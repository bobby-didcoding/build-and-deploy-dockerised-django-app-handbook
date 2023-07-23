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


class Product:
    """
    This handles all API calls to Stripes Product endpoint
    """

    def __init__(self, product):
        self.product = product
        self.external_id = product.external_id

    def all(self):
        """
        Docs - https://stripe.com/docs/api/products/list?lang=python
        """
        obj = stripe.Product.list()
        return obj

    def get(self):
        """
        Docs - https://stripe.com/docs/api/products/retrieve?lang=python
        """
        obj = stripe.Product.retrieve(
            self.external_id,
        )
        return obj

    @method_decorator(override_settings(SUSPEND_SIGNALS=True))
    def post(self):
        """
        Docs - https://stripe.com/docs/api/products/create?lang=python
        """
        obj = stripe.Product.create(
            name=self.product.title,
            url=self.product.get_full_url(),
            metadata={"internal_id": self.product.id},
            default_price_data={
                "currency": "GBP",
                "unit_amount": self.product.price.stripe_amount,
            },
        )
        self.product.external_id = obj["id"]
        self.product.save()

        self.product.price.external_id = obj["default_price"]
        self.product.price.save()
        return obj

    def put(self):
        """
        Docs - https://stripe.com/docs/api/products/modify?lang=python
        """
        obj = stripe.Product.modify(
            self.external_id,
            name=self.product.title,
            url=self.product.get_full_url(),
        )
        return obj

    def delete(self):
        """
        Docs - https://stripe.com/docs/api/products/delete?lang=python
        """

        obj = stripe.Product.delete(
            self.external_id,
        )
        return obj
