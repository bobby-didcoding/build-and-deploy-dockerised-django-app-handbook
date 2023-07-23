# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django.views import generic
from django.contrib.auth import login
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.conf import settings
from django.http import JsonResponse
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import get_connection

# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------
from users.forms import SignupForm

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.mixins import (
    AjaxFormMixin,
    recaptcha_form_submission,
    AccountActivationTokenGenerator,
)


class SignUpView(AjaxFormMixin, generic.FormView):
    """
    Basic view for user sign up with reCAPTURE security
    """

    template_name = "users/sign_up.html"
    form_class = SignupForm
    success_url = "/members/account/"

    # over write the mixin logic to get, check and save reCAPTURE score
    # send a verification email via Celery
    def form_valid(self, form):
        response = super(AjaxFormMixin, self).form_valid(form)
        data = {"result": "Error", "message": "Something went wrong", "redirect": False}
        if self.request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
            token = form.cleaned_data.get("recaptcha_token")
            if not recaptcha_form_submission(token):
                data["message"] = "We could not validate your form submission"
                return JsonResponse(data)

            user = form.save()
            login(
                self.request, user, backend="django.contrib.auth.backends.ModelBackend"
            )

            token = AccountActivationTokenGenerator()
            make_token = token.make_token(user)
            url_safe = urlsafe_base64_encode(force_bytes(user.pk))

            # construct an activation email using bespoke email template
            site_id = settings.SITE_ID
            current_site = Site.objects.get(id=site_id).domain
            if settings.PRODUCTION:
                protocol = "https://"
            else:
                protocol = "http://"
            context = {
                "token": make_token,
                "url_safe": url_safe,
                "domain": f"{protocol}{current_site}",
                "support_email": settings.EMAIL_HOST_USER,
            }

            html_content = render_to_string(
                "users/emails/activation-email.html", context
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
                    "Activation email",
                    text_content,
                    f"{settings.DISPLAY_NAME} <{settings.EMAIL_HOST_USER}>",
                    [user.email],
                    cc=[],
                    bcc=[],
                    connection=connection,
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()

            data.update(
                {
                    "result": "Success",
                    "message": "Thank you for signing up, please activate your account",
                    "redirect": "/",
                }
            )
            return JsonResponse(data)

        return response
