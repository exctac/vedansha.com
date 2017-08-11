from django.conf.urls import url
from article.views import ArticleDetail, ArticleListView

urlpatterns = [
    url(r'^blog/$', ArticleListView.as_view(), name='blog'),
    url(r'^blog/(?P<alias>[-\w]+)/$', ArticleDetail.as_view(), name='blog_article'),
    url(r'^(?P<alias>[-\w]+)/$', ArticleDetail.as_view(), name='article'),
]