import os
from ast import literal_eval

from .defaults import *  # noqa


BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = False

ADMINS = (
    ('Fabien Loffredo', 'flo@atolcd.com'),
)

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1").split(",")

EMAIL_HOST = 'localhost'

SERVER_EMAIL = "noreply@fabienloffredo.com"

DEFAULT_FROM_EMAIL = SERVER_EMAIL

EMAIL_BACKEND = os.environ.get(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("POSTGRESQL_DB", "wcp"),
        'USER': os.getenv("POSTGRESQL_USER", "wcp"),
        'PASSWORD': os.getenv("POSTGRESQL_PASSWORD", "wcp"),
        'HOST': os.getenv("POSTGRESQL_HOST", "127.0.0.1"),
        'PORT': os.getenv("POSTGRESQL_PORT", "5432"),
    }
}

DEFAULT_SECRET_KEY = '3zym&07y8+n2xhlg%g*as@poysqn@5-92hqa2-*i+%3mfjm5gi'
SECRET_KEY = os.getenv("SECRET_KEY", DEFAULT_SECRET_KEY)

STATIC_ROOT = os.path.join(BASE_DIR, 'static/static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

MEDIA_URL = "/media/"

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

SITE_ID = os.environ.get("SITE_ID", 1)

if literal_eval(os.getenv("ENABLE_HTTPS", "True")):
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

if os.getenv("SENTRY_DSN"):
    RAVEN_CONFIG = {
        'dsn': os.getenv("SENTRY_DSN"),
        'release': '0.0.0',
    }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',  # noqa
            'tags': {'custom-tag': 'x'},
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.getenv("LOG_FILE", "wcp.log"),
            'formatter': 'verbose'
        },
    },
    'loggers': {
        '': {
            'level': 'INFO',
            'handlers': ['sentry', 'file'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['sentry', 'file'],
            'propagate': False,
        },
        'raven': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'INFO',
            'handlers': ['file'],
            'propagate': False,
        },
    },
}
