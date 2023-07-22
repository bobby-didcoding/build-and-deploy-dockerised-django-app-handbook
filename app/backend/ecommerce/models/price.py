# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model, ExternalID


class Price(ExternalID, Model):
    interval_count = models.IntegerField(
        _("interval count"), default=1, null=True, blank=True
    )

    amount = models.FloatField(_("amount"), default=1.0)

    @property
    def stripe_amount(self):
        return int(self.amount * 100)
