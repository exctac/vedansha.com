from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from article.models import Article, CategoryArticle

from django_mptt_admin.admin import DjangoMpttAdmin


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article
        widgets = {
            'text': CKEditorUploadingWidget,
        }
        fields = '__all__'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    fieldsets = (
        (None, {
            'fields': (
                ('status', 'show_homepage'),
                ('create_date', 'show_date'),
                'title',
                'alias',
                'subtitle',
                'category',
                ('image', 'image_alt', 'show_image'),
                'text',
                'icons_group',
            )
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
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

    save_on_top = True

    def save_model(self, request, obj, form, change):
        articles_show_homepage = Article.objects.filter(show_homepage=True)
        for article in articles_show_homepage:
            article.show_homepage = False
            article.save()
        super(ArticleAdmin, self).save_model(request, obj, form, change)


@admin.register(CategoryArticle)
class CategoryArticleAdmin(DjangoMpttAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'parent',
                'alias',
                ('image', 'image_alt'),
            )
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )
    list_display = (
        'title',
        'status'
    )
    list_editable = (
        'status',
    )
    save_on_top = True
