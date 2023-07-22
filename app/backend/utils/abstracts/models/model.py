# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import uuid

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
)


class Model(TimeStampedModel, ActivatorModel, models.Model):
    """
    We use this is EVERY db entry
    """

    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True
        ordering = ["created"]
