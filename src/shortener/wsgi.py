"""
WSGI config for yektanet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ENVIRONMENT = os.getenv('YEKTANET_ENV', 'local')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortener.settings.' + ENVIRONMENT)

application = get_wsgi_application()
