# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='alias',
            field=models.CharField(blank=True, max_length=255, verbose_name='Alias'),
        ),
    ]
