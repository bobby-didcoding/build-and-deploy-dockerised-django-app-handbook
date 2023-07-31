# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Policy


class PolicyView(generic.DetailView):
    """
    DetailView used for our Policy page.

    **Template:**

    :template:`core/policy.html`
    """

    model = Policy
    template_name = "core/policy.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f"{self.get_object().title}"
        return context
