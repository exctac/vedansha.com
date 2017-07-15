from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.db import models
from django.contrib import admin
from news.models import News


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        widgets = {
            'text': CKEditorUploadingWidget,
        }
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    fieldsets = (
        (None, {
            'fields': (
                'status',
                ('create_date', 'show_date'),
                'title',
                'alias',
                'subtitle',
                ('image', 'show_image'),
                'text',
                'icons_group',
            )
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )
    list_display = ['title', 'status']
    list_editable = ['status']