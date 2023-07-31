# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from core.models import Blog, Portfolio, Certificate, Testimonial, Skill


class HomeView(generic.TemplateView):
    """
    TemplateView used for our home page.

    **Template:**

    :template:`core/index.html`
    """

    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs"] = Blog.objects.active()
        context["portfolio"] = Portfolio.objects.active()
        context["certificates"] = Certificate.objects.active()
        context["testimonials"] = Testimonial.objects.active()
        context["skills"] = Skill.objects.active()

        return context
