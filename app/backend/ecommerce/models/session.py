# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import ExternalID, Model
from utils.fields.enums import SessionMode, SessionStatus


# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Customer, SessionItem

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_enumfield.enum import EnumField


class Session(ExternalID, Model):
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("session customer"),
        related_name="session_customer",
    )

    session_items = models.ManyToManyField(
        SessionItem,
        verbose_name=_("session items"),
        blank=True,
        related_name="session_session_items",
    )

    session_mode = EnumField(
        SessionMode,
        blank=True,
        null=True,
        verbose_name=_("session mode"),
        default=SessionMode.payment,
    )
    session_status = EnumField(
        SessionStatus,
        blank=True,
        null=True,
        verbose_name=_("session status"),
        default=SessionStatus.open,
    )

    @property
    def empty_cart(self):
        cart = self.customer.cart_customer
        for p in cart.products.all():
            cart.products.remove(p)
        cart.save()

    def get_url(self):
        site_id = settings.SITE_ID
        current_site = Site.objects.get(id=site_id).domain
        if settings.PRODUCTION:
            protocol = "https://"
        else:
            protocol = "http://"
        url = f"{protocol}{current_site}"
        return url

    def get_success_url(self):
        url = self.get_url()
        success_url = f"{url}/session-success/{self.id}/"
        return success_url

    def get_cancelled_url(self):
        url = self.get_url()
        cancel_url = f"{url}/session-cancelled/{self.id}/"
        return cancel_url
