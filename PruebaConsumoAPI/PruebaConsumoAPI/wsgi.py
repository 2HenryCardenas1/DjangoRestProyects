"""
WSGI config for PruebaConsumoAPI project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PruebaConsumoAPI.settings')

dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), 'pokemon/.env')
)


application = get_wsgi_application()
