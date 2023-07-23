# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Portfolio


class PortfolioView(generic.DetailView):
    """
    DetailView used for our Portfolio page.

    **Template:**

    :template:`core/portfolio.html`
    """

    model = Portfolio
    template_name = "core/portfolio.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f"{self.get_object().title}"
        return context
