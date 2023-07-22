# --------------------------------------------------------------
# Python imports
# --------------------------------------------------------------
import os

# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db import models
from django.utils.translation import gettext_lazy as _

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.abstracts import Model

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import TitleSlugDescriptionModel


def testimonial_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/testimonials/<slug>/<filename>
    return os.path.join("testimonials", str(instance.slug), filename)


class Testimonial(TitleSlugDescriptionModel, Model):
    """
    Our Testimonial model.
    """

    image = models.ImageField(
        _("image"), upload_to=testimonial_directory_path, default="default_image.jpg"
    )

    def __str__(self):
        return f"{self.title}"
