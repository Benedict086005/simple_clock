"""WSGI entry point for the Simple Clock project."""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_clock.settings')

application = get_wsgi_application()
