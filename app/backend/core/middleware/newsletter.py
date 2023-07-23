# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.http import JsonResponse
from django.utils.decorators import async_only_middleware

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from core.models import NewsLetter
from utils.mixins import reCAPTCHAValidation, FormErrors
from core.forms import GenericNewsLetterForm


class NewsLetterFormMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    @async_only_middleware
    def process_view(self, request, *args, **kwargs):
        data = {"result": "Error", "message": "Something went wrong", "redirect": False}
        # if the top login form has been posted
        if (
            request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
            and "is_generic_nl_form" in request.POST
        ):
            form = GenericNewsLetterForm(data=request.POST)
            if form.is_valid():
                token = form.cleaned_data.get("nl_recaptcha_token")
                captcha = reCAPTCHAValidation(token)
                if captcha["success"]:
                    # is the email already registered?
                    nl_email = form.cleaned_data.get("nl_email")
                    nl = NewsLetter.objects.filter(nl_email=nl_email)
                    if nl.exists():
                        data = {
                            "result": "Warning",
                            "message": "This email has already been used.",
                        }
                        return JsonResponse(data)
                    form.save()
                    data = {
                        "result": "Success",
                        "message": "We hope you enjoy our newsletter.",
                    }
                    return JsonResponse(data)
                else:
                    data = {
                        "result": "Error",
                        "message": "There was an error, please try again",
                    }
                    return JsonResponse(data)
            else:
                message = FormErrors(form)
                data = {"result": "Error", "message": message}
                return JsonResponse(data)

        request.generic_nl_form = GenericNewsLetterForm()
        return None
