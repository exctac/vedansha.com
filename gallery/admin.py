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
    inlines = [
        VideoGalleryLinkTabular
    ]


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    inlines = [
        PhotoInline
    ]
