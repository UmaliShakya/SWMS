"""
WSGI config for app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swms.settings')
os.makedirs(settings.STATIC_ROOT, exist_ok=True)

application = get_wsgi_application()
