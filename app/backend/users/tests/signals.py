# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.test import TestCase
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from ecommerce.models import Cart, Customer

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.tests import BaseTestCustomUser


User = get_user_model()


class CustomUserSignalTestCase(TestCase, BaseTestCustomUser):
    """
    Test suite for CustomUser signals
    """

    def test_active_customuser_creation_presave_signal(self):
        user = self.get_test_inactive_user()
        self.assertTrue(isinstance(user, User))
        self.assertEqual(Customer.objects.all().count(), 0)
        self.assertEqual(Cart.objects.all().count(), 0)

        user.is_active = False
        user.save()
        self.assertEqual(Customer.objects.all().count(), 0)
        self.assertEqual(Cart.objects.all().count(), 0)

        user.is_active = True
        user.save()
        self.assertEqual(Customer.objects.all().count(), 1)
        self.assertEqual(Cart.objects.all().count(), 1)

        self.assertTrue(isinstance(user.customer_user, Customer))
        self.assertTrue(isinstance(Customer.objects.first().cart_customer, Cart))
