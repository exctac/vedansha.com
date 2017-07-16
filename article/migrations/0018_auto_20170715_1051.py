# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20170715_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='article',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='categoryarticle',
            name='meta_description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='categoryarticle',
            name='meta_keywords',
            field=models.TextField(blank=True, verbose_name='Keywords'),
        ),
        migrations.AddField(
            model_name='categoryarticle',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Title'),
        ),
    ]