# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import logging

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


def print_webhook_event(obj, action):
    try:
        if len(obj) > 0:
            obj = obj[0]
            obj_content_type = ContentType.objects.get_for_model(obj)
            print_text = f"🌐 Webhook event 🌐 - obj:{obj_content_type.app_label}.{obj_content_type.model}, action:{action}"
            logger.info(print_text)
    except (TypeError, AttributeError):
        pass
