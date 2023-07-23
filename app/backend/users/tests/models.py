# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.utils import override_settings


# --------------------------------------------------------------
# App Party imports
# --------------------------------------------------------------
from users.tests import BaseTestCustomUser


User = get_user_model()


@override_settings(SUSPEND_SIGNALS=True)
class CustomUserTestCase(TestCase, BaseTestCustomUser):
    """
    Test suite for CustomUser
    """

    def test_active_customuser_creation(self):
        user = self.get_test_active_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), "Test Case")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_inactive_customuser_creation(self):
        user = self.get_test_inactive_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), "Test Case")
        self.assertEqual(user.is_active, False)
        self.assertEqual(user.is_staff, False)
        self.assertEqual(user.is_superuser, False)

    def test_superuser_customuser_creation(self):
        user = self.get_test_superuser()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), "Test Case")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, True)

    def test_staff_customuser_creation(self):
        user = self.get_test_staff()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(user.__str__(), "Test Case")
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_staff, True)
        self.assertEqual(user.is_superuser, False)

    def test_activate_user_method(self):
        user = self.get_test_inactive_user()
        self.assertEqual(user.is_active, False)
        user.activate_user
        self.assertEqual(user.is_active, True)

    def test_get_full_name_method(self):
        user = self.get_test_inactive_user()
        self.assertEqual(user.get_full_name(), "Test Case")
