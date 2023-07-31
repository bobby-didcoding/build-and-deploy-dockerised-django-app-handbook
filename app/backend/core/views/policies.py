# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Policy


class PoliciesView(generic.ListView):
    """
    ListView used for our Polices page.

    **Template:**

    :template:`core/policies.html`
    """

    model = Policy
    template_name = "core/policies.html"
    paginate_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
