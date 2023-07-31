# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import get_random_string, get_random_email

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.forms import (
    ContactForm,
    GenericNewsLetterForm,
)


class ContactFormTestCase(TestCase):
    """
    Test suite for ContactForm
    """

    def setUp(self):
        self.form_data = {
            "name": "Bobby Stearman",
            "email": "test@case.com",
            "message": "This is a test message",
            "recaptcha_token": "dummy-token",
        }

    def test_contact_form_expected_form_submission(self):
        form_data = self.form_data
        form = ContactForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_contact_form_incorrect_email_submission(self):
        form_data = self.form_data.update({"email": "1234"})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_no_email_submission(self):
        form_data = self.form_data.update({"email": ""})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_exceed_max_length_email_submission(self):
        form_data = self.form_data.update({"email": get_random_email(256)})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_no_name_submission(self):
        form_data = self.form_data.update({"name": ""})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_exceed_max_length_name_submission(self):
        form_data = self.form_data.update({"name": get_random_string(101)})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_no_message_submission(self):
        form_data = self.form_data.update({"message": ""})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_exceed_max_length_message_submission(self):
        form_data = self.form_data.update({"message": get_random_string(1001)})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_contact_form_no_recaptcha_token_submission(self):
        form_data = self.form_data.update({"recaptcha_token": ""})
        form = ContactForm(data=form_data)

        self.assertFalse(form.is_valid())


class GenericNewsLetterFormTestCase(TestCase):
    """
    Test suite for GenericNewsLetterForm
    """

    def setUp(self):
        self.form_data = {
            "nl_email": "test@case.com",
            "nl_recaptcha_token": "dummy-token",
            "is_generic_nl_form": True,
        }

    def test_generic_newsletter_form_expected_form_submission(self):
        form_data = self.form_data
        form = GenericNewsLetterForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_generic_newsletter_form_incorrect_email_submission(self):
        form_data = self.form_data.update({"nl_email": "1234"})
        form = GenericNewsLetterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_generic_newsletter_form_no_email_submission(self):
        form_data = self.form_data.update({"email": ""})
        form = GenericNewsLetterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_generic_newsletter_form_exceed_max_length_email_submission(self):
        form_data = self.form_data.update({"nl_email": get_random_email(256)})
        form = GenericNewsLetterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_generic_newsletter_form_no_recaptcha_token_submission(self):
        form_data = self.form_data.update({"nl_recaptcha_token": ""})
        form = GenericNewsLetterForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_generic_newsletter_form_no_is_generic_nl_form_submission(self):
        form_data = self.form_data.update({"is_generic_nl_form": ""})
        form = GenericNewsLetterForm(data=form_data)

        self.assertFalse(form.is_valid())
