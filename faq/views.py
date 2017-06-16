from django.views.generic import ListView

from common.views import ShowOnlyPublishedView
from faq.models import Faq


class FaqListView(ShowOnlyPublishedView, ListView):
    template_name = 'faq/list.html'
    model = Faq
    title = 'FAQ'
