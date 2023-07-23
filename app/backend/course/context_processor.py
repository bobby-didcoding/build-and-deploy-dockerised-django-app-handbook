# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.conf import settings

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from core.models import Policy


def project_context(request):
    context = {
        "recaptcha_site_key": settings.RECAPTCHA_PUBLIC_KEY,
        "cookie_bot": settings.COOKIE_BOT,
        "privacy_policy": Policy.objects.active()
        .filter(title="Privacy Policy")
        .first(),
        "cookie_policy": Policy.objects.active().filter(title="Cookie Policy").first(),
        "terms_of_service": Policy.objects.active()
        .filter(title="Terms of Service")
        .first(),
        "production": settings.PRODUCTION,
        "my_twitter": "https://twitter.com/didcoding",
        "my_facebook": "https://www.facebook.com/didcoding",
        "my_linkedin": "www.linkedin.com/in/bobby-stearman-6a6ba749",
    }

    return context
