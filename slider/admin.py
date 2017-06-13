from django.contrib import admin
from slider.models import Slide, Slider


class SlideInline(admin.TabularInline):
    model = Slide
    extra = 0


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    inlines = [
        SlideInline
    ]
    list_display = ['name']
