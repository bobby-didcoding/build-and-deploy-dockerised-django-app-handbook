# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import recaptcha_form_submission

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import RequestPasswordForm


def forgotten_password(request):
    if (
        request.method == "POST"
        and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    ):
        form = RequestPasswordForm(request.POST)
        data = {
            "result": "Error",
            "message": "Something went wrong, please try again",
            "redirect": False,
        }
        if form.is_valid():
            token = form.cleaned_data.get("recaptcha_token")
            if not recaptcha_form_submission(token):
                data["message"] = "We could not validate your form submission"
                return JsonResponse(data)
            form.save()
            data.update(
                {
                    "result": "Success",
                    "message": "check your email for a change password link.",
                    "redirect": "/login/",
                }
            )
            return JsonResponse(data)
        else:
            data["message"] = "Form is Not valid! Please Check your passwords"
            return JsonResponse(data)
    else:
        form = RequestPasswordForm()
        return render(request, "users/forgotten_password.html", context={"form": form})
