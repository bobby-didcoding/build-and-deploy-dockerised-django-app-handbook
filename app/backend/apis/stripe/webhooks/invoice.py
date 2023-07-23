# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import logging

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from ecommerce.models import Invoice, Customer

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from apis.stripe import print_webhook_event


logger = logging.getLogger(__name__)


class InvoiceWebhook:
    def __init__(self, data, method):
        self.method = method
        self.data = data
        self.external_id = self.data["id"]

    def get(self):
        inv, created = Invoice.objects.get_or_create(external_id=self.external_id)
        return inv

    def deleted(self):
        obj = self.get()
        print_webhook_event(obj, "deleted")
        obj.status = 0
        obj.save()

    def created(self):
        kwargs = {
            "customer": Customer.objects.get(external_id=self.data["customer"]),
            "hosted_invoice_url": self.data["hosted_invoice_url"],
            "invoice_pdf": self.data["invoice_pdf"],
        }

        obj = Invoice.objects.create(**kwargs)
        print_webhook_event(obj, "created")
