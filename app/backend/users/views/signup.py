# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.contrib.auth import login
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.http import JsonResponse

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import SignupForm

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import (
    AjaxFormMixin,
    recaptcha_form_submission,
    AccountActivationTokenGenerator,
)
from tasks.tasks import create_email


class SignUpView(AjaxFormMixin, generic.FormView):
    """
    Basic view for user sign up with reCAPTURE security
    """

    template_name = "users/sign_up.html"
    form_class = SignupForm
    success_url = "/members/account/"

    # over write the mixin logic to get, check and save reCAPTURE score
    # send a verification email via Celery
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        data = {"result": "Error", "message": "Something went wrong", "redirect": False}
        if self.request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            token = form.cleaned_data.get("recaptcha_token")
            if not recaptcha_form_submission(token):
                data["message"] = "We could not validate your form submission"
                return JsonResponse(data)

            user = form.save()
            login(
                self.request, user, backend="django.contrib.auth.backends.ModelBackend"
            )

            token = AccountActivationTokenGenerator()
            make_token = token.make_token(user)
            url_safe = urlsafe_base64_encode(force_bytes(user.pk))

            kwargs = {
                "user_id": user.id,
                "subject": "Course - Activate your Account!",
                "context": {
                    "token": make_token,
                    "url_safe": url_safe,
                },
                "template": "users/emails/activation-email.html",
            }
            create_email.run(**kwargs)

            data.update(
                {
                    "result": "Success",
                    "message": "Thank you for signing up, please activate your account",
                    "redirect": "/",
                }
            )
            return JsonResponse(data)

        return response
