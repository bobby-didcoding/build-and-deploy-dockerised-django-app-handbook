# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Blog


class BlogView(generic.DetailView):
    """
    DetailView used for our Blog page.

    **Template:**

    :template:`core/blog.html`
    """

    model = Blog
    template_name = "core/blog.html"

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_name"] = f"{self.get_object().title}"
        return context
