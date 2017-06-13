from django.contrib import admin
from article.models import Article
from ckeditor.widgets import CKEditorWidget
from django.db import models


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }