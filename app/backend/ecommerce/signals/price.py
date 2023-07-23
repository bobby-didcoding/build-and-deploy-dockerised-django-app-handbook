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
from ecommerce.models import Price


@suspendingreceiver(post_save, sender=Price, weak=False)
def create_price(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe price
        """
        pass
