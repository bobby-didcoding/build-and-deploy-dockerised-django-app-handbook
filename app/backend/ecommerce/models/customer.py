# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model, ExternalID


User = get_user_model()


class Customer(ExternalID, Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="customer_user",
    )

    default_source = models.CharField(
        _("default source"), max_length=100, blank=True, null=True
    )

    def __str__(self):
        return f"{self.user}"
