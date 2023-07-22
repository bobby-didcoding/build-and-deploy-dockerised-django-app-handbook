# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import six
import random
import string

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.tokens import PasswordResetTokenGenerator


# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import requests


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = "".join(random.choice(letters) for i in range(length))
    return result_str


def get_random_email(length):
    random_string = f"{get_random_string(length)}.com"
    half_length = int(round(length / 2, 0))
    result_str = f"{random_string[:half_length]}@{random_string[half_length:]}"
    return result_str


def reCAPTCHAValidation(token):
    """reCAPTCHA validation"""
    result = requests.post(
        "https://www.google.com/recaptcha/api/siteverify",
        data={"secret": settings.RECAPTCHA_PRIVATE_KEY, "response": token},
    )

    return result.json()


def FormErrors(*args):
    """
    Handles form error that are passed back to AJAX calls
    """
    message = ""
    for f in args:
        if f.errors:
            message = f.errors.as_text()
    return message


class AjaxFormMixinBase(object):
    """
    Mixin to ajaxify django form - can be over written in view by calling form_invalid method
    """

    def form_invalid(self, form):
        response = super(AjaxFormMixinBase, self).form_invalid(form)
        if self.request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            return JsonResponse(
                {"result": "Error", "message": FormErrors(form), "redirect": False}
            )
        return response


"""
Mixin to ajaxify django form - can be over written in view by calling form_valid method
"""


class AjaxFormMixin(AjaxFormMixinBase):
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        if self.request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            form.save()
            return JsonResponse({"result": "Success", "message": "Thank you."})
        return response


class RecaptchaAjaxFormMixin(AjaxFormMixinBase):
    # over write the mixin logic to get, check and save reCAPTURE score
    def form_valid(self, form):
        response = super(RecaptchaAjaxFormMixin, self).form_valid(form)
        if self.request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            token = form.cleaned_data.get("recaptcha_token")
            captcha = reCAPTCHAValidation(token)
            if captcha["success"]:
                form.save()
                data = {"result": "Success", "message": "Thank you."}
                return JsonResponse(data)
            else:
                data = {
                    "result": "Error",
                    "message": "There was an error, please try again",
                }
                return JsonResponse(data)
        return response


def recaptcha_form_submission(token):
    captcha = reCAPTCHAValidation(token)
    if captcha["success"]:
        return True
    return False


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk)
            + six.text_type(timestamp)
            + six.text_type(user.is_active)
        )
