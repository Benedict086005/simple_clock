from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-change-me-in-real-projects"
DEBUG = True
ALLOWED_HOSTS = []

# Only our own app plus Django's static file helper.
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "clock",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "simple_clock.urls"

WSGI_APPLICATION = "simple_clock.wsgi.application"

# Where Django looks for HTML templates.
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
    },
]

# Static files (CSS, images) live in clock/static/
STATIC_URL = "static/"

# The server returns its local time.
TIME_ZONE = "Africa/Lagos"
USE_TZ = True
