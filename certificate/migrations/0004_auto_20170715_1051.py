# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0003_certificate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='meta_keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]
