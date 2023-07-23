# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import get_random_email, get_random_string

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import (
    LoginForm,
    SignupForm,
    RequestPasswordForm,
)


class LoginFormTestCase(TestCase):
    """
    Test suite for LoginForm
    """

    def setUp(self):
        self.form_data = {
            "email": "test@case.com",
            "password": "123456",
            "recaptcha_token": "dummy-token",
        }

    def test_login_form_expected_form_submission(self):
        form_data = self.form_data
        form = LoginForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_login_form_incorrect_email_submission(self):
        form_data = self.form_data.update({"email": "1234"})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_form_no_email_submission(self):
        form_data = self.form_data.update({"email": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_form_exceed_max_length_email_submission(self):
        form_data = self.form_data.update({"email": get_random_email(256)})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_form_no_password_submission(self):
        form_data = self.form_data.update({"password": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_login_form_no_recaptcha_token_submission(self):
        form_data = self.form_data.update({"recaptcha_token": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())


class SignupFormTestCase(TestCase):
    """
    Test suite for SignupForm
    """

    def setUp(self):
        self.form_data = {
            "email": "test@case.com",
            "first_name": "Test",
            "last_name": "Case",
            "password1": "123456",
            "password2": "123456",
            "recaptcha_token": "dummy-token",
        }

    def test_signup_form_expected_form_submission(self):
        form_data = self.form_data
        form = SignupForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_signup_form_incorrect_email_submission(self):
        form_data = self.form_data.update({"email": "1234"})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_email_submission(self):
        form_data = self.form_data.update({"email": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_exceed_max_length_email_submission(self):
        form_data = self.form_data.update({"email": get_random_email(256)})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_first_name_submission(self):
        form_data = self.form_data.update({"first_name": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_exceed_max_length_first_name_submission(self):
        form_data = self.form_data.update({"first_name": get_random_string(151)})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_last_name_submission(self):
        form_data = self.form_data.update({"last_name": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_exceed_max_length_last_name_submission(self):
        form_data = self.form_data.update({"last_name": get_random_string(151)})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_password1_submission(self):
        form_data = self.form_data.update({"password1": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_password2_submission(self):
        form_data = self.form_data.update({"password2": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_signup_form_no_recaptcha_token_submission(self):
        form_data = self.form_data.update({"recaptcha_token": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())


class RequestPasswordFormTestCase(TestCase):
    """
    Test suite for RequestPasswordForm
    """

    def setUp(self):
        self.form_data = {"email": "test@case.com", "recaptcha_token": "dummy-token"}

    def test_request_password_form_expected_form_submission(self):
        form_data = self.form_data
        form = RequestPasswordForm(data=form_data)

        self.assertTrue(form.is_valid())

    def test_request_password_form_incorrect_email_submission(self):
        form_data = self.form_data.update({"email": "1234"})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_request_password_form_no_email_submission(self):
        form_data = self.form_data.update({"email": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_request_password_form_exceed_max_length_email_submission(self):
        form_data = self.form_data.update({"email": get_random_email(256)})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())

    def test_request_password_form_no_recaptcha_token_submission(self):
        form_data = self.form_data.update({"recaptcha_token": ""})
        form = RequestPasswordForm(data=form_data)

        self.assertFalse(form.is_valid())
