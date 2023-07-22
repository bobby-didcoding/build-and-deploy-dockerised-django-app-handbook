# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import admin
from core.models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
