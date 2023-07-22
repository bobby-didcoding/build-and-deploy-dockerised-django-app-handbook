# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model, ExternalID

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Price, Customer, Product


class SessionItem(ExternalID, Model):
    price = models.ForeignKey(
        Price,
        verbose_name=_("price"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="session_price",
    )

    product = models.ForeignKey(
        Product,
        verbose_name=_("product"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="session_product",
    )

    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("session item customer"),
        related_name="sessionitem_customer",
    )

    def __str__(self):
        return f"{self.price} - {self.quantity}"

    @property
    def quantity(self):
        return 1
