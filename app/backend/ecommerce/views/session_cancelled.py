# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Session


class SessionCancelledView(generic.DetailView):
    """
    Template that displays all active items in shop.

    **Template:**

    :template:`ecommerce/session_cancelled.html`
    """

    template_name = "ecommerce/session_cancelled.html"

    model_object = Session

    def get(self, request, session_id, *args, **kwargs):
        obj = get_object_or_404(self.model_object, id=session_id)
        obj.delete()
        context = {}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
