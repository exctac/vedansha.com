from django.views.generic import DetailView, ListView, TemplateView
from article.models import Article, CategoryArticle
from common.models import AbstractStatus


class ArticleDetail(DetailView):
    template_name = "article/article_page.html"
    model = Article
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'


class CategoryList(ListView):
    """
    
    """
    def get_queryset(self):
        catalog_slug = self.kwargs.setdefault('catalog_alias', None)
        subcatalog_slug = self.kwargs.setdefault('subcatalog_alias', None)

        if subcatalog_slug:
            subcategory = CategoryArticle.objects.filter(alias=subcatalog_slug)[0]
            queryset = Article.objects.filter(category=subcategory, status=AbstractStatus.PUBLISHED)
        else:
            queryset = CategoryArticle.objects.get(alias=catalog_slug).get_children().filter(status=AbstractStatus.PUBLISHED)
        return queryset

    def get_template_names(self):
        subcatalog_slug = self.kwargs.setdefault('subcatalog_alias', None)

        if subcatalog_slug:
            return ['article/article_list.html']
        return ['article/category_list.html']
