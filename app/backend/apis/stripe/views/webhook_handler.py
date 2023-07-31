# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import json
import logging

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from apis.stripe import (
    CustomerWebhook,
    InvoiceWebhook,
)

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)


@csrf_exempt
def stripe_webhooks(request):

    if settings.STRIPE_WEBHOOK_KEY:
        try:
            sig_header = request.META['HTTP_STRIPE_SIGNATURE']
            event = None
            payload = request.body
            endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
            try:
                event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
                )
            except ValueError as e:
                # Invalid payload
                return HttpResponse(status=400)
            except stripe.error.SignatureVerificationError as e:
                # Invalid signature
                return HttpResponse(status=400)
        except KeyError:
            return HttpResponse(status=404) 

    if request.method == "POST":
        try:
            payload = request.body
            event = json.loads(payload)
        except ValueError as e:
            logging.error(
                "❌🌐 Failed to process webhook while parsing basic request." + str(e)
            )
            return JsonResponse({"success": True}, status=400)

        event_list = event["type"].split(".")
        if len(event_list) == 3:
            del event_list[0]

        match event_list[0]:
            case "customer":
                handler = CustomerWebhook(event["data"]["object"], event_list[1])
            case "invoice":
                handler = InvoiceWebhook(event["data"]["object"], event_list[1])
            case _:
                handler = None
        if handler:
            if hasattr(handler, event_list[1]):
                getattr(handler, event_list[1])()
        return HttpResponse(status=200)
    return HttpResponse(status=404)
