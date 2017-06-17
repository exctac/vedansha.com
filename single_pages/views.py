from single_pages.models import *
from article.models import Article
from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = "single_pages/contacts.html"

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['article'] = Contacts.get_solo()
        return context
