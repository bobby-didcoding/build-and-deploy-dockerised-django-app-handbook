# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.utils.translation import gettext_lazy as _
from django.db import models

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Customer, Product, Session, SessionItem

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model


class Cart(Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        verbose_name=_("user"),
        related_name="cart_customer",
    )

    products = models.ManyToManyField(
        Product, blank=True, related_name="cart_products", verbose_name=_("products")
    )

    @property
    def total(self):
        count = 0
        for p in self.products.all():
            count += p.price.amount
        return count

    @property
    def stripe_amount(self):
        return int(self.total * 100)

    def create_session_item(self, product):
        session_item = SessionItem.objects.create(
            customer=self.customer, price=product.price, product=product
        )
        return session_item

    def create_session(self):
        session = Session.objects.create(
            customer=self.customer,
        )
        for p in self.products.all():
            session.session_items.add(self.create_session_item(p))
        session.save()
        return session
