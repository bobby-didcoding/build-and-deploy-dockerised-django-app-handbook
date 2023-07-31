# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Portfolio


class PortfoliosView(generic.ListView):
    """
    ListView used for our Portfolio page.

    **Template:**

    :template:`core/portfolios.html`
    """

    model = Portfolio
    template_name = "core/portfolios.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
