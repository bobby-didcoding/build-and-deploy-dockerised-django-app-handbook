# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from core.models import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
