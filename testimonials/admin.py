from django.contrib import admin
from testimonials.models import Testimonials
from bleach import clean


@admin.register(Testimonials)
class SliderAdmin(admin.ModelAdmin):
    fields = ('status', 'title', 'text',)
    list_display = [
        'title',
        'short_text',
        'status',
    ]
    list_editable = [
        'status',
    ]

    def short_text(self, obj):
        return clean(obj.text[:120], strip=True) + ' ...'
    short_text.short_description = "testimonial's short text"
