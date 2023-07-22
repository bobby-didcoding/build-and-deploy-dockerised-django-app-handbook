# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model


class NewsLetter(Model):
    nl_email = models.EmailField(_("newsletter email"), max_length=255)

    def __str__(self):
        return f"{self.nl_email}"
