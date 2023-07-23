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


# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from apis.stripe import (
    CustomerWebhook,
    InvoiceWebhook,
)

logger = logging.getLogger(__name__)


@csrf_exempt
def stripe_webhooks(request):
    # We will protect this view with a VPN
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
