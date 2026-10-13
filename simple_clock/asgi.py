"""ASGI entry point for the Simple Clock project."""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_clock.settings')

application = get_asgi_application()
