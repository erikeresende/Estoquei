import os
from django.core.asgi import get_asgi_application

# Define the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estoque_project.settings')

# Initialize the ASGI application
application = get_asgi_application()
