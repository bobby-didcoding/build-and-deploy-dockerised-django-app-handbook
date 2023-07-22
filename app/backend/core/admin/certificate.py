# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from core.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
