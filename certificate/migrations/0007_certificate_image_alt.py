# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_auto_20170715_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='image_alt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Image alternative text'),
        ),
    ]