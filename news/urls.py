from django.conf.urls import url
from article.views import ArticleDetail
from news.views import NewsListView
from news.models import News

urlpatterns = [
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<alias>[-\w]+)/$', ArticleDetail.as_view(
        model=News
    ), name='news_detail'),
]