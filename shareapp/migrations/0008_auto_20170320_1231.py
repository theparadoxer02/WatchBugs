# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 12:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0007_auto_20170320_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugshare',
            name='bug',
            field=models.CharField(blank=True, max_length=1000000, null=True),
        ),
        migrations.AlterField(
            model_name='bugshare',
            name='code',
            field=models.CharField(max_length=1000000, null=True),
        ),
    ]
