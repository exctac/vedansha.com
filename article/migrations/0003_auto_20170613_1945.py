# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20170613_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='alias',
            field=models.CharField(default=None, max_length=255, verbose_name='Alias'),
        ),
    ]
