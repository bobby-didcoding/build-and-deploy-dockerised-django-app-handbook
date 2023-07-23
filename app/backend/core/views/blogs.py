# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Blog


class BlogsView(generic.ListView):
    """
    ListView used for our blogs page.

    **Template:**

    :template:`core/blogs.html`
    """

    model = Blog
    template_name = "core/blogs.html"
    paginate_by = 100

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")
