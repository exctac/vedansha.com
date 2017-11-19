from django.views.generic import ListView
from news.models import News
from common.views import ShowOnlyPublishedView


class NewsListView(ShowOnlyPublishedView, ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'
    paginate_by = 12
