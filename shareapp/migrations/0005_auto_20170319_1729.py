# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0004_auto_20170312_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugshare',
            name='bug',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bugshare',
            name='comment',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
