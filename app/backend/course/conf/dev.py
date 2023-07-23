# --------------------------------------------------------------
# Python  imports
# --------------------------------------------------------------
import os
import socket

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
    EMAIL_BACKEND,
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_USE_TLS,
    EMAIL_HOST_USER,
    DISPLAY_NAME,
    EMAIL_HOST_PASSWORD,
    EMAIL_SUPPORT_EMAIL,
    RECAPTCHA_PUBLIC_KEY,
    RECAPTCHA_PRIVATE_KEY,
    COOKIE_BOT,
    STRIPE_SECRET_KEY,
    STRIPE_PUBLISHABLE,
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
AUTH_USER_MODEL = AUTH_USER_MODEL
EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS
EMAIL_HOST_USER = EMAIL_HOST_USER
DISPLAY_NAME = DISPLAY_NAME
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_SUPPORT_EMAIL = EMAIL_SUPPORT_EMAIL
RECAPTCHA_PUBLIC_KEY = RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = RECAPTCHA_PRIVATE_KEY
COOKIE_BOT = COOKIE_BOT
STRIPE_SECRET_KEY = STRIPE_SECRET_KEY
STRIPE_PUBLISHABLE = STRIPE_PUBLISHABLE

PRODUCTION = 0
DEBUG = 1

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

# --------------------------------------------------------------
# DEBUG TOOLBAR SETTINGS
# --------------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]
# --------------------------------------------------------------
# END DEBUG TOOLBAR SETTINGS
# --------------------------------------------------------------
