from django.conf.urls import url
from article.views import ArticleDetail
from team.views import MemberDetail, MemberListView
from team.models import Member

urlpatterns = [
    url(r'^team/$', MemberListView.as_view(), name='team_list'),
    url(r'^team/(?P<alias>[-\w]+)$', ArticleDetail.as_view(
        model=Member
    ), name='team_detail'),
]