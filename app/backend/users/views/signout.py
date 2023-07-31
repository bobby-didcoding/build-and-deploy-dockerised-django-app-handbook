# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def logout_user(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect("core:home")
