# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-13 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_image_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='meta_title',
            field=models.CharField(blank=True, help_text='If this field is empty, it dublicate Article Title.', max_length=255, verbose_name='Title'),
        ),
    ]
