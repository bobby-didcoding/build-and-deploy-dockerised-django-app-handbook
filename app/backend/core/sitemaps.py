# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import sitemaps
from django.urls import reverse

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Policy, Blog, Portfolio


class CoreStaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            "core:home",
            "core:contact",
            "core:policies",
            "core:blog",
            "core:portfolio",
        ]

    def location(self, item):
        return reverse(item)


class PolicySiteMap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Policy.objects.active()


class BlogSiteMap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Blog.objects.active()


class PortfolioSiteMap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Portfolio.objects.active()
