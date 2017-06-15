# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonials',
            old_name='testimonial',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='testimonials',
            name='author',
        ),
        migrations.AddField(
            model_name='testimonials',
            name='title',
            field=models.CharField(default=None, max_length=255, verbose_name='Testimonial title'),
            preserve_default=False,
        ),
    ]