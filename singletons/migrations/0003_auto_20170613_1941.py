# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-13 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singletons', '0002_copyright_listicons_listiconsitem_yogaalliance_yogaallianceimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listiconsitem',
            name='color',
            field=models.CharField(blank=True, choices=[('gray-light', 'gray-light'), ('gray', 'gray'), ('green', 'green'), ('yellow', 'yellow'), ('orange', 'orange'), ('blue ', 'blue ')], max_length=20, verbose_name='Header color'),
        ),
        migrations.AlterField(
            model_name='listiconsitem',
            name='icon',
            field=models.CharField(blank=True, choices=[('lotus', 'Lotus'), ('om-symbol', 'Om symbol'), ('skype', 'Skype'), ('views', 'Views'), ('cube-questions-mark', 'Cube questions'), ('moon', 'Moon')], max_length=20, verbose_name='Icon'),
        ),
    ]
