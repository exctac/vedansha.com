from django.views.generic import ListView, DetailView, TemplateView

from common.views import ShowOnlyPublishedView
from gallery.models import PhotoGallery, VideoGallery


class PhotoGalleryListView(ShowOnlyPublishedView, ListView):
    template_name = 'gallery/photo_gallery_list.html'
    model = PhotoGallery


class PhotoGalleryDetailView(DetailView):
    model = PhotoGallery
    template_name = 'gallery/photo_gallery_detail.html'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'


class VideoGalleryTemplateView(TemplateView):
    template_name = 'gallery/video_gallery.html'

    def get_context_data(self, **kwargs):
        context = super(VideoGalleryTemplateView, self).get_context_data(**kwargs)
        context['video_gallery'] = VideoGallery.get_solo().get_videos()
        print(context['video_gallery'])
        return context
