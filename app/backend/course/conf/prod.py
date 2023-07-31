# --------------------------------------------------------------
# Python  imports
# --------------------------------------------------------------
import os
import logging.config

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
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    CELERY_ACCEPT_CONTENT,
    CELERY_RESULT_SERIALIZER,
    CELERY_TASK_SERIALIZER,
    CELERY_BEAT_SCHEDULER,
)

# --------------------------------------------------------------
# Django  imports
# --------------------------------------------------------------
from django.utils.log import DEFAULT_LOGGING
from django.core.management.color import supports_color

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
CELERY_BROKER_URL = CELERY_BROKER_URL
CELERY_RESULT_BACKEND = CELERY_RESULT_BACKEND
CELERY_ACCEPT_CONTENT = CELERY_ACCEPT_CONTENT
CELERY_RESULT_SERIALIZER = CELERY_RESULT_SERIALIZER
CELERY_TASK_SERIALIZER = CELERY_TASK_SERIALIZER
CELERY_BEAT_SCHEDULER = CELERY_BEAT_SCHEDULER

PRODUCTION = 1
DEBUG = 0
CSRF_TRUSTED_ORIGINS = [f'http://{h}' for h in ALLOWED_HOSTS]

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

# --------------------------------------------------------------
# Cache settings
# --------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f'{os.environ.get("CELERY_BROKER")}/0',
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}
# --------------------------------------------------------------
# END CACHE SETTINGS
# --------------------------------------------------------------

# --------------------------------------------------------------
# LOGGING SETTINGS
# --------------------------------------------------------------
LOGGING_CONFIG = None
LOGLEVEL = os.environ.get("LOGLEVEL", "DEBUG" if DEBUG else "INFO").upper()
LOGFILEPATH = os.environ.get("LOGFILEPATH", "logs/app.log")
CELERYLOGFILEPATH = os.environ.get("CELERYLOGFILEPATH", "logs/celery.log")
CELERY_TASKS_LOGGER_NAME = "celery_tasks"

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "console": {
                "format": "[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "course.json.formatter": {"class": "utils.logger.courseJsonFormatter"},
            'colorlog': {
                'class': 'colorlog.ColoredFormatter',
                'format': '%(log_color)s[%(asctime)s,%(msecs)03d %(levelname)s %(filename)s:%(lineno)s|%(name)s] %(message)s',
                'datefmt': "%Y-%m-%d %H:%M:%S",
            },
            "django.server": {
                "()": "django.utils.log.ServerFormatter",
                "format": "[{asctime}] {message}",
                "datefmt": "%Y-%m-%d %H:%M:%S",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "colorlog.StreamHandler"
                if supports_color()
                else "logging.StreamHandler",
                "formatter": "colorlog" if supports_color() else "console",
            },
            "rotating_file": {
                "class": "utils.logger.BetterRotatingFileHandler",
                "formatter": "course.json.formatter",
                "filename": LOGFILEPATH,
                "maxBytes": 1024 * 1024 * 10,
                "backupCount": 10,
            },
            "celery_rotating_file": {
                "class": "utils.logger.BetterRotatingFileHandler",
                "formatter": "course.json.formatter",
                "filename": CELERYLOGFILEPATH,
                "maxBytes": 1024 * 1024 * 10,
                "backupCount": 10,
            },
            "django.server": DEFAULT_LOGGING["handlers"]["django.server"],
        },
        "loggers": {
            # "root" logger which serves as a catch-all for any logs that are sent from any Python module
            "": {
                "level": LOGLEVEL,
                "handlers": ["console", "rotating_file"],
            },
            "django": {
                "handlers": ["console", "rotating_file"],
                "level": LOGLEVEL,
            },
            "django.request": {
                "handlers": ["console", "rotating_file"],
                "level": LOGLEVEL,
                "propagate": False,
            },
            "django.db.backends": {
                "handlers": ["console", "rotating_file"],
                "level": LOGLEVEL,
                "propagate": False,
            },
            # Logging From Your Application
            "course": {
                "level": LOGLEVEL,
                "handlers": ["console", "rotating_file"],
                "propagate": False,
            },
            "users": {
                "level": LOGLEVEL,
                "handlers": ["console", "rotating_file"],
                "propagate": False,
            },
            "ecommerce": {
                "level": LOGLEVEL,
                "handlers": ["console", "rotating_file"],
                "propagate": False,
            },
            "core": {
                "level": LOGLEVEL,
                "handlers": ["console", "rotating_file"],
                "propagate": False,
            },
            CELERY_TASKS_LOGGER_NAME: {
                "level": LOGLEVEL,
                "handlers": ["console", "celery_rotating_file"],
                "propagate": False,
            },
            "django.server": DEFAULT_LOGGING["loggers"]["django.server"],
        },
    }
)
# --------------------------------------------------------------
# LOGGING SETTINGS END
# --------------------------------------------------------------
