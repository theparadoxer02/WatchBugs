# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0005_auto_20170319_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bugshare',
            name='url',
        ),
    ]
