# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "customer")
