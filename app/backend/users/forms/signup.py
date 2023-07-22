# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()


class SignupForm(forms.ModelForm):
    recaptcha_token = forms.CharField(widget=forms.HiddenInput())
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Write your password",
                "class": "form-control password",
            }
        ),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your password",
                "class": "form-control password",
            }
        ),
    )
    first_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "form-control"}
        ),
    )
    last_name = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Last name", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email name", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
