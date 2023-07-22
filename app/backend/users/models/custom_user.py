# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import (
    Model,
)

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.managers import CustomUserManager


# This is the new custom user model
class CustomUser(AbstractBaseUser, Model, PermissionsMixin):
    """
    CustomUser
    This is our custom user model.
    We are extending the built-in User model in Django.
    """

    email = models.EmailField(
        _("email address"), unique=True, help_text=_("rogerredhat@oddersea.com")
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    @property
    def activate_user(self):
        """
        Basic method to activate a user
        """
        self.is_active = True
        return self

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()
