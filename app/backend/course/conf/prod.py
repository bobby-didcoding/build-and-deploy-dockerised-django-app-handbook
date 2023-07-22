# --------------------------------------------------------------
# Python  imports
# --------------------------------------------------------------
import os

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from .common import (
    BASE_DIR,
    SECRET_KEY,
    ALLOWED_HOSTS,
    RUN_SERVER_PORT,
    INSTALLED_APPS,
    SITE_ID,
    DATABASES,
    MIDDLEWARE,
    ROOT_URLCONF,
    TEMPLATES,
    WSGI_APPLICATION,
    AUTH_PASSWORD_VALIDATORS,
    LANGUAGE_CODE,
    TIME_ZONE,
    USE_I18N,
    USE_TZ,
    DEFAULT_AUTO_FIELD,
    SUSPEND_SIGNALS,
    AUTH_USER_MODEL,
)

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

load_dotenv()

BASE_DIR = BASE_DIR
SECRET_KEY = SECRET_KEY
ALLOWED_HOSTS = ALLOWED_HOSTS
RUN_SERVER_PORT = RUN_SERVER_PORT
INSTALLED_APPS = INSTALLED_APPS
SITE_ID = SITE_ID
DATABASES = DATABASES
MIDDLEWARE = MIDDLEWARE
ROOT_URLCONF = ROOT_URLCONF
TEMPLATES = TEMPLATES
WSGI_APPLICATION = WSGI_APPLICATION
AUTH_PASSWORD_VALIDATORS = AUTH_PASSWORD_VALIDATORS
LANGUAGE_CODE = LANGUAGE_CODE
TIME_ZONE = TIME_ZONE
USE_I18N = USE_I18N
USE_TZ = USE_TZ
DEFAULT_AUTO_FIELD = DEFAULT_AUTO_FIELD
SUSPEND_SIGNALS = SUSPEND_SIGNALS
AUTH_USER_MODEL = AUTH_USER_MODEL

PRODUCTION = 1
DEBUG = 0

# --------------------------------------------------------------
# STATICFILES SETTINGS
# --------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]
AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = f"https://{os.environ.get('AWS_S3_ENDPOINT_URL')}"
AWS_S3_CUSTOM_DOMAIN = (
    f"{AWS_STORAGE_BUCKET_NAME}.{os.environ.get('AWS_S3_ENDPOINT_URL')}"
)
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_LOCATION = os.environ.get("AWS_LOCATION")
AWS_MEDIA_LOCATION = os.environ.get("AWS_MEDIA_LOCATION")
AWS_DEFAULT_ACL = "public-read"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATIC_URL = "{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
MEDIA_URL = "{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
# --------------------------------------------------------------
# END STATICFILES SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# START SENTRY SETTINGS
# --------------------------------------------------------------
sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DNS"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)
# --------------------------------------------------------------
# END SENTRY SETTINGS
# --------------------------------------------------------------
