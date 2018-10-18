# Turn off bytecode generation
import sys
from asgiref.sync import sync_to_async
from django.core.wsgi import get_wsgi_application


sys.dont_write_bytecode = True

# Django specific settings
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
import django

django.setup()

from db import models


def print_all_models():
    return models.Sample.objects.all()


@sync_to_async
def _create_record(name):
    return models.Sample.objects.create(name=name)


async def create_record(name=None):
    await _create_record(name)
