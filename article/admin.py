from django.contrib import admin
from article.models import Article
from ckeditor.widgets import CKEditorWidget
from django.db import models


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        'status',
        ('create_date', 'show_date'),
        'title',
        'alias',
        'subtitle',
        'image',
        'text',
        'icons_group',
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }