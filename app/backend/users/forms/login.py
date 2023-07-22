# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate


User = get_user_model()


class LoginForm(forms.Form):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput())
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control password"}
        ),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
    )

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     user = authenticate(email=email, password=password)
    #     if not user or not user.is_active:
    #         raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
    #     return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = authenticate(email=email, password=password)
        return user
