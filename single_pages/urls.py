from django.conf.urls import url
from article.views import ArticleDetail
from single_pages.views import *

urlpatterns = [
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
    url(r'^donation/$', ArticleDetail.as_view(
        template_name='single_pages/donation.html',
    ), {'alias': 'donation'}, name='donation'),
    url(r'^booking-form/$', BookingTemplateView.as_view(), name="booking_form"),
    url(r'^resources/$', ResourcesView.as_view(), name="resources"),
]