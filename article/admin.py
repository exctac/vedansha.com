from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from article.models import Article, CategoryArticle
from django.db import models
from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = (
        'status',
        ('create_date', 'show_date'),
        'title',
        'alias',
        'subtitle',
        'category',
        ('image', 'show_image'),
        'text',
        'icons_group',
    )
    list_display = (
        'title',
        'category',
        'status'
    )
    list_editable = (
        'category',
        'status'
    )
    list_filter = ('category',)

    formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }
    save_on_top = True

@admin.register(CategoryArticle)
class CategoryArticleAdmin(DjangoMpttAdmin):
    list_display = (
        'title',
        'status'
    )
    list_editable = (
        'status',
    )
    save_on_top = True
