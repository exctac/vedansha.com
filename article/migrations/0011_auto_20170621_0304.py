# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-21 03:04
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20170618_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(help_text='Main picture of the article (optional field)', upload_to='articles/', verbose_name='Image'),
        ),
    ]