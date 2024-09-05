"""
WSGI config for estoque_project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/X.X/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Define a variável de ambiente DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estoque_project.settings')

# Obtém a aplicação WSGI
application = get_wsgi_application()
