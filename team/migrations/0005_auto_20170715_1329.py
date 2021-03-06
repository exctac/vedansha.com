# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20170708_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='member',
            name='meta_keywords',
            field=models.TextField(blank=True, help_text='Keywords are written comma-separated, for example "word 1, word 2, word 3, ..."', verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='member',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]
