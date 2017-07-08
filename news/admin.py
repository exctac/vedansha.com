from django.db import models
from django.contrib import admin
from news.models import News
from ckeditor.widgets import CKEditorWidget


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_editable = ['status']
    fields = (
        'status',
        ('create_date', 'show_date'),
        'title',
        'alias',
        'subtitle',
        ('image', 'show_image'),
        'text',
        'icons_group',
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }