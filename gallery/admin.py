from django.contrib import admin
from solo.admin import SingletonModelAdmin
from gallery.models import PhotoGallery, Photo, VideoGallery, VideoGalleryLink


class VideoGalleryLinkTabular(admin.TabularInline):
    model = VideoGalleryLink
    extra = 0


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


@admin.register(VideoGallery)
class VideoGalleryAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )
    inlines = [
        VideoGalleryLinkTabular
    ]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
           'fields': ('status', ('title', 'alias',))
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )
    inlines = [
        PhotoInline
    ]
