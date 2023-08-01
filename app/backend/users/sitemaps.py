# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import sitemaps
from django.urls import reverse


class UsersStaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["users:login", "users:signup"]

    def location(self, item):
        return reverse(item)
