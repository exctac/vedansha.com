# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-08 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import easy_thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Published'), ('u', 'Unpublished')], default='u', help_text='Select a status publish.', max_length=1, verbose_name='Status')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='slider', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Published'), ('u', 'Unpublished')], default='u', help_text='Select a status publish.', max_length=1, verbose_name='Status')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('alias', models.CharField(blank=True, max_length=255, verbose_name='Alias')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='slide',
            name='slider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slider.Slider'),
        ),
    ]
