# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import post_save, pre_save
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import suspendingreceiver
from apis.stripe import StripeCustomer

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Customer


User = get_user_model()


@suspendingreceiver(post_save, sender=Customer, weak=False)
def create_customer(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe customer
        """
        StripeCustomer(instance).post()


@suspendingreceiver(pre_save, sender=User, weak=False)
def update_customer(sender, instance, **kwargs):
    if Customer.objects.filter(user=instance).exists():
        try:
            current = instance
            current_fields = [current.email, current.get_full_name()]
            previous = sender.objects.get(id=instance.id)
            previous_fields = [previous.email, previous.get_full_name()]

            if previous_fields != current_fields:
                customer = instance.customer_user
                StripeCustomer(customer).put()
        except (sender.DoesNotExist,):
            pass
