from __future__ import unicode_literals

from django.apps import AppConfig


class ShareappConfig(AppConfig):
    name = 'shareapp'

    def ready(self):
        from shareapp import signals
