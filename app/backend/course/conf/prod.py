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
)

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from dotenv import load_dotenv

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

PRODUCTION = 1
DEBUG = 0
CSRF_TRUSTED_ORIGINS = [f'https://{h}' for h in ALLOWED_HOSTS]

# --------------------------------------------------------------
# STATICFILES SETTINGS
# --------------------------------------------------------------
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "media"),
]

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
# --------------------------------------------------------------
# END STATICFILES SETTINGS
# --------------------------------------------------------------
