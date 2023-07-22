# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import post_save

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import suspendingreceiver

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Invoice


@suspendingreceiver(post_save, sender=Invoice, weak=False)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe invoice
        """
        pass
