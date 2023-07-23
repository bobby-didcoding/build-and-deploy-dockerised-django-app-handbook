# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.utils.encoding import force_str
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_decode

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import AccountActivationTokenGenerator


account_activation_token = AccountActivationTokenGenerator()
User = get_user_model()


def activate(request, uidb64, token):
    """
    Activate a user from an email link
    """
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("core:home")
    else:
        return HttpResponse("Invalid")
