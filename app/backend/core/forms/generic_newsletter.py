# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import NewsLetter


class GenericNewsLetterForm(forms.ModelForm):
    """
    Basic model-form for our newsletter model that can be used across all views
    """

    nl_email = forms.EmailField(
        max_length=255,
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Email address", "class": "form-control"}
        ),
    )

    nl_recaptcha_token = forms.CharField(widget=forms.HiddenInput())

    is_generic_nl_form = forms.CharField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = NewsLetter
        fields = ("nl_email",)
