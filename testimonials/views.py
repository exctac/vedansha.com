from django.views.generic import ListView

from common.views import ShowOnlyPublishedView
from testimonials.models import Testimonials


class TestimonialsView(ShowOnlyPublishedView, ListView):
    template_name = 'testimonials/testimonials.html'
    model = Testimonials
    context_object_name = 'testimonials'
