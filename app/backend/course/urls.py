# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views import defaults as default_views
from users.forms import EmailValidationOnForgotPassword
from django.contrib.sitemaps.views import sitemap

from core.sitemaps import (
    CoreStaticViewsSitemap,
    PolicySiteMap,
    BlogSiteMap,
    PortfolioSiteMap,
)

from users.sitemaps import (
    UsersStaticViewsSitemap,
)
from ecommerce.sitemaps import EcommerceStaticViewsSitemap, ProductSiteMap

sitemaps = {
    "core_sitemap": CoreStaticViewsSitemap,
    "ecommerce_sitemap": EcommerceStaticViewsSitemap,
    "users_sitemap": UsersStaticViewsSitemap,
    "policies": PolicySiteMap,
    "blogs": BlogSiteMap,
    "portfolio": PortfolioSiteMap,
    "products": ProductSiteMap,
}

handler400 = "course.views.handler400"
handler403 = "course.views.handler403"
handler404 = "course.views.handler404"
handler500 = "course.views.handler500"
handler503 = "course.views.handler503"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", include("core.urls", namespace="core")),
    path("", include("ecommerce.urls", namespace="ecommerce")),
    path("", include("users.urls", namespace="users")),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            form_class=EmailValidationOnForgotPassword
        ),
        name="reset_password",
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]

if not settings.PRODUCTION:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Course Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Dashboard"
