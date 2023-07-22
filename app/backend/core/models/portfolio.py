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
from utils.abstracts import Model, RichTextModel

# --------------------------------------------------------------
# 3rd party imports
# --------------------------------------------------------------
from django_extensions.db.models import TitleSlugDescriptionModel


def portfolio_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/portfolio/<slug>/<filename>
    return os.path.join("portfolio", str(instance.slug), filename)


class Portfolio(TitleSlugDescriptionModel, RichTextModel, Model):
    """
    Our Portfolio model.
    """

    image = models.ImageField(
        _("image"), upload_to=portfolio_directory_path, default="default_image.jpg"
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/portfolio/{self.slug}"
