from django.views.generic import DetailView
from article.models import Article


class ArticleDetail(DetailView):
    template_name = "article.html"
    model = Article
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetail, self).get_context_data()
        return context
