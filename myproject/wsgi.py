import os
from django.core.wsgi import get_wsgi_application
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
env_file = os.environ.get('ENV_FILE', '.env')
if os.path.exists(env_file):
    from dotenv import load_dotenv
    load_dotenv(env_file)

application = get_wsgi_application()

# """
# WSGI config for myproject project.

# It exposes the WSGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
# """

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# application = get_wsgi_application()
