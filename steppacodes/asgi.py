from decouple import config 
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'steppacodes.settings.{config("SETTINGS")}')

application = get_asgi_application()
