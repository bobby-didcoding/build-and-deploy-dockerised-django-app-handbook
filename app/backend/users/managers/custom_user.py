# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        super_user = self.create_user(
            email, first_name, last_name, password, **other_fields
        )

        return super_user

    def create_user(self, email, first_name, last_name, password, **other_fields):
        # email validation
        if not email:
            raise ValueError(_("You must provide an email address"))
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name, **other_fields
        )
        user.set_password(password)
        user.save()
        return user
