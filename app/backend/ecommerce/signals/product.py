# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import logging

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import pre_save

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import suspendingreceiver
from apis.stripe import StripeProduct

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product

logger = logging.getLogger(__name__)


@suspendingreceiver(pre_save, sender=Product, weak=False)
def manage_product(sender, instance, **kwargs):
    if not instance.price:
        raise Exception("Please add price")
    try:
        current = instance
        previous = sender.objects.get(id=instance.id)

        if previous.title != current.title:
            StripeProduct(current).put()

        if previous.price != current.price:
            raise Exception(
                "You can not change the price once set, please create a new product"
            )
    except (sender.DoesNotExist,):
        StripeProduct(current).post()
