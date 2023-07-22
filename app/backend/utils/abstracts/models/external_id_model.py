# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _


class ExternalID(models.Model):
    class Meta:
        abstract = True

    external_id = models.CharField(
        _("external id"), max_length=100, blank=True, null=True
    )
