# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.decorators import suspendingreceiver

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from ecommerce.models import Invoice


User = get_user_model()


@suspendingreceiver(post_save, sender=Invoice, weak=False)
def create_invoice(sender, instance, created, **kwargs):
    if created:
        """
        Create a stripe invoice
        """
        site_id = settings.SITE_ID
        current_site = Site.objects.get(id=site_id).domain
        if settings.PRODUCTION:
            protocol = "https://"
        else:
            protocol = "http://"
        context = {
            "invoice_url": instance.hosted_invoice_url,
            "domain": f"{protocol}{current_site}",
            "support_email": settings.EMAIL_HOST_USER,
        }

        html_content = render_to_string(
            "ecommerce/emails/invoice-email.html", context
        )  # render with dynamic value
        text_content = strip_tags(
            html_content
        )  # Strip the html tag. So people can see the pure text at least.

        with get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD,
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            msg = EmailMultiAlternatives(
                "New invoice",
                text_content,
                f"{settings.DISPLAY_NAME} <{settings.EMAIL_HOST_USER}>",
                [instance.customer.user.email],
                cc=[],
                bcc=[],
                connection=connection,
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
