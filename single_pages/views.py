from single_pages.models import *
from django.views.generic import TemplateView, FormView
from single_pages.forms import ContactForm
from django.core.mail import send_mail

from vedansha import settings


class ContactsView(FormView):
    template_name = "single_pages/contacts.html"
    success_url = '/contacts/'
    form_class = ContactForm

    def form_valid(self, form):
        send_mail("subject", 'message', settings.EMAIL_HOST_USER, ['info@vedansha.com'])
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return super(ContactsView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['article'] = Contacts.get_solo()
        return context


class BookingTemplateView(TemplateView):
    template_name = "single_pages/booking_form.html"
