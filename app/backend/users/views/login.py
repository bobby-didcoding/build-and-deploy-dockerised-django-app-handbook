# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import JsonResponse

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import recaptcha_form_submission, FormErrors
from users.forms import LoginForm


def login_user(request):
    """
    User to sign-in a user
    """
    if request.GET.get("next", None) or request.POST.get("next", None):
        if request.method == "POST":
            redirect_url = request.POST.get("next", None)
        else:
            redirect_url = request.GET.get("next", None)
    else:
        redirect_url = "/"
    if (
        request.method == "POST"
        and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    ):
        form = LoginForm(request.POST)
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

            user = form.login(request)
            if user is None:
                data["message"] = "Please check your email and password"
                return JsonResponse(data)
            if user is not None and user.is_active:
                data["redirect"] = redirect_url
                login(request, user)
                data.update({"result": "Success", "message": "You are logged in"})

                return JsonResponse(data)
            else:
                data["message"] = "You have not activated your account"
                return JsonResponse(data)

        else:
            data["message"] = FormErrors(form)
            return JsonResponse(data)
    else:
        if request.user.is_authenticated:
            return redirect(redirect_url)
        form = LoginForm()
        return render(request, "users/login.html", context={"form": form})
