# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import RecaptchaAjaxFormMixin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.forms import ContactForm


class ContactView(RecaptchaAjaxFormMixin, generic.FormView):

    """
    FormView used for our home page.

    **Template:**

    :template:`core/contact.html`
    """

    template_name = "core/contact.html"
    form_class = ContactForm
    success_url = "/"
