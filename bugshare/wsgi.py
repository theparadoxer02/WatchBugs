"""
WSGI config for bugshare project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import django
django.setup()
import django
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bugshare.settings")

application = get_wsgi_application()

from shareapp.models import *
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

import django
django.setup()
