from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from team.models import Member
from django.db import models


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'status',
    )
    list_editable = ('status',)
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
