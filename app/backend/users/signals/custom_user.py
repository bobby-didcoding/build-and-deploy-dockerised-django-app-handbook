# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from ecommerce.models import Customer, Cart
from utils.decorators import suspendingreceiver


User = get_user_model()


@suspendingreceiver(pre_save, sender=User, weak=False)
def create_ecommerce_objects(sender, instance, **kwargs):
    try:
        current = instance
        previous = sender.objects.get(id=instance.id)
        if not previous.is_active and current.is_active:
            customer = Customer.objects.create(user=instance)
            Cart.objects.create(customer=customer)

    except sender.DoesNotExist:
        pass
