from django.conf.urls import url
from article.views import ArticleDetail
from single_pages.views import *

urlpatterns = [
    url(r'^contacts/$', ContactsView.as_view(), name='contacts'),
    url(r'^donation/$', ArticleDetail.as_view(
        template_name='single_pages/donation.html',
    ), {'alias': 'donation'}, name='donation'),
]