# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import TitleSlugDescriptionModel


class Skill(TitleSlugDescriptionModel, Model):
    """
    Our Skill model.
    """

    score = models.IntegerField(_("score"))

    def __str__(self):
        return f"{self.title}"
