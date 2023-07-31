# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
import os
from pathlib import Path

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from dotenv import load_dotenv

load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")


# Application definition
RUN_SERVER_PORT = 8000

# --------------------------------------------------------------
# Installed apps
# --------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    "django.contrib.sites",
]


THIRD_PARTY_APPS = [
    "ckeditor",
    "django_extensions",
    "debug_toolbar",
]

APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + APPS
SITE_ID = 1
# --------------------------------------------------------------
# End Installed apps
# --------------------------------------------------------------

# --------------------------------------------------------------
# DATABASE SETTINGS
# --------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("DB_NAME", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("DB_USER", "user"),
        "PASSWORD": os.environ.get("DB_PASSWORD", "password"),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
# --------------------------------------------------------------
# END DATABASE SETTINGS
# --------------------------------------------------------------

MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "course.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # PROJECT CONTEXT
            ],
        },
    },
]

WSGI_APPLICATION = "course.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SUSPEND_SIGNALS = False

# --------------------------------------------------------------
# EMAIL SETTINGS
# --------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS")
if EMAIL_USE_TLS:
    EMAIL_USE_TLS = True
else:
    EMAIL_USE_TLS = False
EMAIL_HOST_USER = os.environ.get("DONOT_REPLY_EMAIL")
DISPLAY_NAME = os.environ.get("EMAIL_DISPLAY_NAME")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_SUPPORT_EMAIL = os.environ.get("SUPPORT_EMAIL")
# --------------------------------------------------------------
# END EMAIL SETTINGS
# --------------------------------------------------------------


# --------------------------------------------------------------
# RECAPTCHA SETTINGS
# --------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = os.environ.get("RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
# --------------------------------------------------------------
# END RECAPTCHA SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# COOKIE SETTINGS
# --------------------------------------------------------------
COOKIE_BOT = os.environ.get("COOKIE_BOT", None)
# --------------------------------------------------------------
# END COOKIE SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# STRIPE SETTINGS
# --------------------------------------------------------------
STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET")
STRIPE_PUBLISHABLE = os.environ.get("STRIPE_PUBLISHABLE")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET", None)
STRIPE_WEBHOOK_KEY = os.environ.get("STRIPE_WEBHOOK_KEY", None)
# --------------------------------------------------------------
# END STRIPE SETTINGS
# --------------------------------------------------------------
