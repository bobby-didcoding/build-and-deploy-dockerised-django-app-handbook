# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model


class Contact(Model):
    name = models.CharField(_("name"), max_length=100)
    email = models.EmailField(_("email"), max_length=255)
    message = models.TextField(_("message"), max_length=1000)

    def __str__(self):
        return f"{self.name}"
