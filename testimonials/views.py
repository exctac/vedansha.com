from django.views.generic import ListView
from single_pages.models import TestimonialsPage
from common.views import ShowOnlyPublishedView
from testimonials.models import Testimonials


class TestimonialsView(ShowOnlyPublishedView, ListView):
    template_name = 'testimonials/testimonials.html'
    model = Testimonials
    context_object_name = 'testimonials'

    def get_context_data(self, **kwargs):
        context = super(TestimonialsView, self).get_context_data(**kwargs)
        context['meta'] = TestimonialsPage.get_solo().as_meta(self.request)
        return context
