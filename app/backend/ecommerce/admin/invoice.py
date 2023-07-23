# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Invoice


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "customer")
