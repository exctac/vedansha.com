from django.conf.urls import url

from testimonials.views import TestimonialsView

urlpatterns = [
    url(r'^$', TestimonialsView.as_view(), name='testimonials_list'),
]