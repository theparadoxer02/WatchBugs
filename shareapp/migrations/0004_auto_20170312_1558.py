# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareapp', '0003_auto_20170312_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugshare',
            name='bug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bugshare',
            name='code',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='bugshare',
            name='url',
            field=models.URLField(max_length=50, null=True),
        ),
    ]
