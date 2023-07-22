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
from ecommerce.models import Product


@suspendingreceiver(post_save, sender=Product, weak=False)
def create_product(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe product
        """
        pass
