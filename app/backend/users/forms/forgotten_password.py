# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model

User = get_user_model()


class RequestPasswordForm(PasswordResetForm):
    """
    Form that uses built-in PasswordResetForm to handel a request to reset password
    """

    recaptcha_token = forms.CharField(widget=forms.HiddenInput())
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Write your email", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = ("email",)
