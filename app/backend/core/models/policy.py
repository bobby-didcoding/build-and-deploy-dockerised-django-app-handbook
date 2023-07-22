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


def policy_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/policies/<slug>/<filename>
    return os.path.join("policies", str(instance.slug), filename)


class Policy(TitleSlugDescriptionModel, RichTextModel, Model):
    """
    Our Policy model. This is used to create policy pages such as cookie and privacy
    """

    class Meta(Model.Meta):
        verbose_name_plural = "Policies"

    image = models.ImageField(
        _("image"), upload_to=policy_directory_path, default="default_image.jpg"
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/policy/{self.slug}"
