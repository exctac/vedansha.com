from django.views.generic import ListView, DetailView, TemplateView

from common.views import ShowOnlyPublishedView, MetaContextMixin
from gallery.models import PhotoGallery, VideoGallery
from single_pages.models import PhotoGalleriesPage


class PhotoGalleryListView(ShowOnlyPublishedView, ListView):
    template_name = 'gallery/photo_gallery_list.html'
    model = PhotoGallery

    def get_context_data(self, **kwargs):
        context = super(PhotoGalleryListView, self).get_context_data(**kwargs)
        context['meta'] = PhotoGalleriesPage.get_solo().as_meta(self.request)
        return context


class PhotoGalleryDetailView(MetaContextMixin, DetailView):
    model = PhotoGallery
    template_name = 'gallery/photo_gallery_detail.html'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'


class VideoGalleryTemplateView(TemplateView):
    template_name = 'gallery/video_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(VideoGalleryTemplateView, self).get_context_data(**kwargs)
        context['video_gallery'] = VideoGallery.get_solo().get_videos()
        context['meta'] = VideoGallery.get_solo().as_meta(self.request)
        return context
