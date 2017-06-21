from django.views.generic import DetailView, ListView
from common.views import ShowOnlyPublishedView
from team.models import Member


class MemberDetail(DetailView):
    template_name = "article/article_page.html"
    model = Member
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'


class MemberListView(ShowOnlyPublishedView, ListView):
    template_name = "team/member_list.html"
    model = Member
