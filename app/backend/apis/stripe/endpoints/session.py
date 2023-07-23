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


class Session:
    """
    This handles all API calls to Stripes Session endpoint
    """

    def __init__(self, session):
        self.session = session
        self.session_external_id = self.session.external_id
        self.session_items = self.session.session_items.all()

    @method_decorator(override_settings(SUSPEND_SIGNALS=True))
    def post(self):
        """
        Docs - https://stripe.com/docs/api/checkout/sessions/create?lang=python
        """

        # Manage line items
        line_items = []
        prices = [s.price.external_id for s in self.session_items]
        unique_prices = list(set(prices))
        for u in unique_prices:
            line_items.append({"price": u, "quantity": prices.count(u)})

        kwargs = {
            "line_items": line_items,
            "customer": self.session.customer.external_id,
            "mode": self.session.session_mode.name,
            "payment_method_types": ["card"],
            "success_url": self.session.get_success_url(),
            "cancel_url": self.session.get_cancelled_url(),
            "invoice_creation": {"enabled": True},
            "metadata": {
                "internal_id": self.session.id,
            },
        }

        obj = stripe.checkout.Session.create(**kwargs)
        self.session.external_id = obj["id"]
        self.session.save()
        return obj

    def delete(self):
        """
        Docs - https://stripe.com/docs/api/checkout/sessions/delete?lang=python
        """

        obj = stripe.checkout.Session.delete(
            self.session_external_id,
        )
        return obj
