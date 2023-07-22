# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "external_id", "created")
