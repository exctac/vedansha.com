from common.views import ShowOnlyPublishedView
from resources.models import BookCategory
from single_pages.models import *
from django.views.generic import TemplateView, FormView, ListView
from single_pages.forms import ContactForm, BookingForm
from common.functions import sender_email
from team.models import Member


class ContactsView(FormView):
    template_name = "single_pages/contacts.html"
    success_url = '/contacts/'
    form_class = ContactForm

    def form_valid(self, form):
        sender_email(form=form, subject="Contacts Form", temp_html='contact.html', temp_text='contact.txt')
        return self.render_to_response(self.get_context_data(form=self.form_class()))

    def form_invalid(self, form):
        return super(ContactsView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['article'] = Contacts.get_solo()
        context['meta'] = Contacts.get_solo().as_meta(self.request)
        return context


class BookingTemplateView(FormView):
    template_name = "single_pages/booking_form.html"
    success_url = '/booking-form/'
    form_class = BookingForm

    def form_valid(self, form):
        sender_email(form=form, subject="Booking Form", temp_html='booking.html', temp_text='booking.txt')
        return self.render_to_response(self.get_context_data(form=self.form_class()))

    def form_invalid(self, form):
        return super(BookingTemplateView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(BookingTemplateView, self).get_context_data(**kwargs)
        context['meta'] = BookingPage.get_solo().as_meta(self.request)
        return context


class MemberListView(ShowOnlyPublishedView, ListView):
    template_name = "team/member_list.html"
    model = Member

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context['meta'] = Members.get_solo().as_meta(self.request)
        return context


class ResourcesView(TemplateView):
    template_name = "single_pages/resources.html"

    def get_context_data(self, **kwargs):
        context = super(ResourcesView, self).get_context_data(**kwargs)
        context['book_categories'] = BookCategory.objects.prefetch_related('book').filter(status=AbstractStatus.PUBLISHED)
        return context
