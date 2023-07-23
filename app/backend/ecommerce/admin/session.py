# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Session


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "external_id")
