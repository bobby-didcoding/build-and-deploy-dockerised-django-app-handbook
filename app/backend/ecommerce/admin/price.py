# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "created")
