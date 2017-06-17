from django.views.generic import DetailView
from article.models import Article


class ArticleDetail(DetailView):
    template_name = "article/article_page.html"
    model = Article
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'