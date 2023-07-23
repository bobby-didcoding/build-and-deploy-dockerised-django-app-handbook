# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce import views

app_name = "ecommerce"

urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path("session-create/", views.session_create, name="session-create"),
    path(
        "session-success/<uuid:session_id>/",
        views.SessionSuccessView.as_view(),
        name="session-success",
    ),
    path(
        "session-cancelled/<uuid:session_id>/",
        views.SessionCancelledView.as_view(),
        name="session-cancelled",
    ),
    path("products/", views.ProductsView.as_view(), name="products"),
    path("product/<str:slug>/", views.ProductView.as_view(), name="product"),
]
