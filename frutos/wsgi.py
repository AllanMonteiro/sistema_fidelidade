"""
WSGI config for frutos project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Define qual arquivo de configuração do Django será usado
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frutos.settings')

application = get_wsgi_application()
