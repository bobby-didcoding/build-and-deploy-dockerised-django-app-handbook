# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from core.models import Portfolio


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
