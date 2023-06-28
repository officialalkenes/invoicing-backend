from .base import *

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", cast=bool)


DATABASES["default"].update(
    DATABASES={
        "default": {
            # "ENGINE": "django_tenants.postgresql_backend",
            "ENGINE": "django.db.backends.postgresql",
            "NAME": config("NAME"),
            "USER": config("USER"),
            "PASSWORD": config("PASSWORD"),
        }
    }
)

# CELERY AND CELERY BEAT
CELERY_BROKER_URL = "redis://127.0.0.1:6379"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_SERIALIZER = "json"
CELERY_TIMEZONE = "Africa/Lagos"


# EMAIL SETUP
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_PORT = ''
# EMAIL_HOST_USER = 'your@djangoapp.com'
# EMAIL_HOST_PASSWORD = 'your-email account-password'
# EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False
# EMAIL_FILE_PATH = "/tmp/messages"  # change this to a proper location

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}