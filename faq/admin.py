from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from faq.models import Faq


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'status')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Faq, FaqAdmin)
