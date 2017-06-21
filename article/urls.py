from django.conf.urls import url
from article.views import ArticleDetail

urlpatterns = [
    url(r'^(?P<alias>[-\w]+)/$', ArticleDetail.as_view(), name='article'),
]