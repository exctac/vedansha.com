# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0005_auto_20170715_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='image_alt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Image alternative text'),
        ),
    ]
