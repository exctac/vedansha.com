from django.conf.urls import url

from gallery.views import PhotoGalleryListView, PhotoGalleryDetailView, VideoGalleryTemplateView

urlpatterns = [
    url(r'^photo-gallery/$', PhotoGalleryListView.as_view(), name='photo_gallery_list'),
    url(r'^photo-gallery/(?P<alias>[-\w]+)$', PhotoGalleryDetailView.as_view(), name='photo_gallery_detail'),
    url(r'^video-gallery/$', VideoGalleryTemplateView.as_view(), name='video_gallery'),
]