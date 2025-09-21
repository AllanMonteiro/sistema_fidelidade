import os
from django.core.asgi import get_asgi_application

# Define qual arquivo de configuração do Django será usado
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'frutos.settings')

application = get_asgi_application()
