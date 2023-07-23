# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.test.client import Client

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import get_random_string, get_random_email

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.tests import BaseTestCustomUser


class UsersViewTestBase(BaseTestCustomUser):

    def setUp(self):

        self.client = Client()
        self.user = self.get_test_active_user()

class SignupTestCase(UsersViewTestBase, TestCase):
    """
    Test suite for SignupView
    """

    def test_signup_view_get_request(self):
        client = self.client
        response = client.get("/signup/")
        
        self.assertEqual(response.status_code, 200)

    def test_signup_view_put_request(self):
        client = self.client
        response = client.put("/signup/")
        
        self.assertEqual(response.status_code, 200)

    def test_signup_view_delete_request(self):
        client = self.client
        response = client.delete("/signup/")
        
        self.assertEqual(response.status_code, 405)


class LoginTestCase(UsersViewTestBase, TestCase):
    """
    Test suite for LoginView
    """

    def test_login_view_get_request(self):
        client = self.client
        response = client.get("/login/")
        
        self.assertEqual(response.status_code, 200)

    def test_login_view_put_request(self):
        client = self.client
        response = client.put("/login/")
        
        self.assertEqual(response.status_code, 200)

    def test_login_view_delete_request(self):
        client = self.client
        response = client.delete("/login/")
        
        self.assertEqual(response.status_code, 200)



class ForgottenPasswordTestCase(UsersViewTestBase, TestCase):
    """
    Test suite for ForgottenPassword
    """

    def test_forgotten_password_view_get_request(self):
        client = self.client
        response = client.get("/forgotten-password/")
        
        self.assertEqual(response.status_code, 200)

    def test_forgotten_password_view_put_request(self):
        client = self.client
        response = client.put("/forgotten-password/")
        
        self.assertEqual(response.status_code, 200)

    def test_forgotten_password_view_delete_request(self):
        client = self.client
        response = client.delete("/forgotten-password/")
        
        self.assertEqual(response.status_code, 200)

class LogoutViewTestCase(UsersViewTestBase, TestCase):
    """
    Test suite for LogoutView
    """

    def test_cart_view_get_request(self):
        self.client.force_login(self.user)
        response = self.client.get("/logout/")
        
        self.assertEqual(response.status_code, 302)
