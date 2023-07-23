# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import SessionItem


@admin.register(SessionItem)
class SessionItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "external_id",
    )
