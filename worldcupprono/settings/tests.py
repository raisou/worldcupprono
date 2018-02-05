import os

from .defaults import *  # noqa

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'travis_ci',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SECRET_KEY = 'zj6ay3l7s^ga3!*!zi(s81+jj01eblt=wxzzd3=__n0wh0a5uw'

LANGUAGE_CODE = "fr-FR"

TIME_ZONE = 'Europe/Paris'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/static/')

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media/')

MEDIA_URL = "/media/"

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
