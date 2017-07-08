# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-08 21:43
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20170625_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='Main picture of the article (optional field)', null=True, upload_to='articles/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='categoryarticle',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='Main picture of the article (optional field)', null=True, upload_to='articles/', verbose_name='Image'),
        ),
    ]
