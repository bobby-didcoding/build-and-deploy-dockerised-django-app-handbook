# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("policies/", views.PoliciesView.as_view(), name="policies"),
    path("policy/<str:slug>/", views.PolicyView.as_view(), name="policy"),
    path("blog/", views.BlogsView.as_view(), name="blog"),
    path("blog/<str:slug>/", views.BlogView.as_view(), name="blog-details"),
    path("portfolio/", views.PortfoliosView.as_view(), name="portfolio"),
    path(
        "portfolio/<str:slug>/", views.PortfolioView.as_view(), name="portfolio-detail"
    ),
]
