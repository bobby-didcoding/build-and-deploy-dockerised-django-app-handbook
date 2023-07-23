# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.contrib import sitemaps
from django.urls import reverse

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product


class EcommerceStaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return [
            "ecommerce:products",
        ]

    def location(self, item):
        return reverse(item)


class ProductSiteMap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.active()
