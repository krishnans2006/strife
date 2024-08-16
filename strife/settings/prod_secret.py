# Rename this file to secret.py to be used in production.

DEBUG = False


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "strife",
        "USER": "strife",
        "PASSWORD": "strife",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}

STATIC_ROOT = "/var/www/strife/static"
MEDIA_ROOT = "/var/www/strife/media"
