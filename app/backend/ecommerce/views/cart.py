# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class CartView(generic.TemplateView):
    """
    TemplateView to display all items in a users cart.

    **Context**

    Stripe publishable key.

    **Template:**

    :template:`ecommerce/cart.html`
    """

    template_name = "ecommerce/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
