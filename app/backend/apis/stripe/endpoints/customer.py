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


class Customer:
    """
    This handles all API calls to Stripes Customer endpoint
    """

    def __init__(self, customer):
        self.customer = customer
        self.external_id = customer.external_id

    def get(self):
        """
        Docs - https://stripe.com/docs/api/customer/retrieve?lang=python
        """
        obj = stripe.Customer.retrieve(
            self.external_id,
        )

        self.customer.default_source = obj["default_source"]
        self.customer.save()
        return obj

    @method_decorator(override_settings(SUSPEND_SIGNALS=True))
    def post(self):
        """
        Docs - https://stripe.com/docs/api/customers/create?lang=python
        """
        obj = stripe.Customer.create(
            email=self.customer.user.email,
            name=self.customer.user.get_full_name(),
            metadata={"internal_id": self.customer.id},
        )
        self.customer.external_id = obj["id"]
        self.customer.save()
        return obj

    def put(self):
        """
        Docs - https://stripe.com/docs/api/customers/modify?lang=python
        """
        obj = stripe.Customer.modify(
            self.external_id,
            email=self.customer.user.email,
            name=self.customer.user.get_full_name(),
        )
        return obj

    def delete(self):
        """
        Docs - https://stripe.com/docs/api/customer/delete?lang=python
        """

        obj = stripe.Customer.delete(
            self.external_id,
        )
        return obj
