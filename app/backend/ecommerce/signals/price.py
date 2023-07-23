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

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Price

logger = logging.getLogger(__name__)


@suspendingreceiver(pre_save, sender=Price, weak=False)
def manage_price(sender, instance, **kwargs):
    try:
        current = instance
        previous = sender.objects.get(id=instance.id)

        if previous.amount != current.amount:
            raise Exception(
                "You can not change the price once set, please create a new product"
            )
    except (sender.DoesNotExist,):
        pass
