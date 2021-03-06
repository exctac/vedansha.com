# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 13:05
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
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Published'), ('u', 'Unpublished')], default='u', help_text='Select a status publish.', max_length=1, verbose_name='Status')),
                ('title', models.CharField(max_length=255, verbose_name='Category title')),
                ('alias', models.CharField(editable=False, max_length=255, verbose_name='Alias')),
                ('image', easy_thumbnails.fields.ThumbnailerImageField(blank=True, help_text='Main picture of the article (optional field)', null=True, upload_to='articles/', verbose_name='Image')),
                ('show_image', models.BooleanField(default=True, verbose_name='Show image?')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('p', 'Published'), ('u', 'Unpublished')], default='u', help_text='Select a status publish.', max_length=1, verbose_name='Status')),
                ('title', models.CharField(max_length=255, verbose_name='Category title')),
                ('alias', models.CharField(editable=False, max_length=255, verbose_name='Alias')),
            ],
            options={
                'verbose_name': 'Book Category',
                'verbose_name_plural': 'Book Categories',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resources.BookCategory'),
        ),
    ]
