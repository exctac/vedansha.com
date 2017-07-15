from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from team.models import Member
from django.db import models


class MemberAdminForm(forms.ModelForm):
    class Meta:
        model = Member
        widgets = {
            'text': CKEditorUploadingWidget,
        }
        fields = '__all__'


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    form = MemberAdminForm
    fieldsets = (
        (None, {
            'fields': (
                'status',
                'title',
                'alias',
                'subtitle',
                ('image', 'show_image'),
                'text',
            )
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )
    list_display = (
        'title',
        'status',
    )
    list_editable = ('status',)
