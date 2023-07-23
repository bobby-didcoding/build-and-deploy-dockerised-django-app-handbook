# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Product


class ProductView(generic.DetailView):
    """
    DetailView used for our Product page.

    **Template:**

    :template:`ecommerce/product.html`
    """

    model = Product
    template_name = "ecommerce/product.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f"{self.get_object().title}"
        return context
