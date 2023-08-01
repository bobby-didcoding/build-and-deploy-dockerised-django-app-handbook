# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import suspendingreceiver
from tasks.tasks import create_email

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Invoice


User = get_user_model()


@suspendingreceiver(post_save, sender=Invoice, weak=False)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe invoice
        """
        kwargs = {
            "user_id": instance.customer.user.id,
            "subject": "Course - New invoice!",
            "context": {"invoice_url": instance.hosted_invoice_url},
            "template": "ecommerce/emails/invoice-email.html",
        }
        create_email.delay(**kwargs)
