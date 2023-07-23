# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import logging

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from ecommerce.models import Customer

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from apis.stripe import print_webhook_event


logger = logging.getLogger(__name__)


class CustomerWebhook:
    def __init__(self, data, method):
        self.method = method
        self.data = data
        self.external_id = self.data["id"]
        self.internal_id = self.data["metadata"]["internal_id"]

    def get(self):
        customer = Customer.objects.filter(id=self.internal_id)
        if customer.exists():
            return customer.first()
        else:
            customer = Customer.objects.filter(external_id=self.external_id)
            if customer.exists():
                return customer.first()
        return None

    def deleted(self):
        obj = self.get()
        print_webhook_event(obj, "deleted")
        obj.status = 0
        obj.save()

    def updated(self):
        obj = self.get()
        print_webhook_event(obj, "updated")

        if self.data["default_source"]:
            obj.default_source = self.data["default_source"]
        obj.save()
