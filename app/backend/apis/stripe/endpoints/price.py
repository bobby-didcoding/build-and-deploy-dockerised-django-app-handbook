# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.utils.decorators import method_decorator
from django.test.utils import override_settings

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Price:
    """
    This handles all API calls to Stripes Price endpoint
    """

    def __init__(self, price):
        self.price = price
        self.price_external_id = price.external_id
        self.product = self.price.product_price.first()
        self.product_external_id = self.product.external_id

    @method_decorator(override_settings(SUSPEND_SIGNALS=True))
    def post(self):
        """
        Docs - https://stripe.com/docs/api/prices/create?lang=python
        """
        price_kwargs = {
            "product": self.product_external_id,
            "currency": "GBP",
            "unit_amount": self.product.price.stripe_amount,
            "metadata": {"internal_id": self.price.id},
        }
        obj = stripe.Price.create(**price_kwargs)

        self.price.external_id = obj["id"]
        self.price.save()
        return obj

    def put(self):
        """
        Docs - https://stripe.com/docs/api/prices/update?lang=python
        """
        price_kwargs = {
            "product": self.product_external_id,
            "currency": "GBP",
            "unit_amount": self.product.price.stripe_amount,
            "metadata": {"internal_id": self.price.id},
        }
        obj = stripe.Price.modify(self.price_external_id, **price_kwargs)

        return obj
