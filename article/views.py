from django.views.generic import DetailView, ListView
from article.models import Article, CategoryArticle
from common.models import AbstractStatus
from common.views import MetaContextMixin, ShowOnlyPublishedView


class ArticleDetail(MetaContextMixin, DetailView):
    template_name = "article/article_page.html"
    model = Article
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'


class CourseDetail(MetaContextMixin, DetailView):
    template_name = "article/article_page.html"
    model = Article
    context_object_name = 'article'
    slug_field = 'alias'
    slug_url_kwarg = 'alias'

    def get_context_data(self, **kwargs):
        context = super(CourseDetail, self).get_context_data(**kwargs)
        category = self.object.category
        if category.parent:
            context['subcatalog'] = category
            context['catalog'] = category.parent
        else:
            context['catalog'] = category
        return context


class CategoryList(ListView):
    """
    
    """
    paginate_by = 12

    def get_queryset(self):
        catalog_slug = self.kwargs.setdefault('catalog_alias', None)
        subcatalog_slug = self.kwargs.setdefault('subcatalog_alias', None)
        if subcatalog_slug:
            subcategory = CategoryArticle.objects.filter(alias=subcatalog_slug)[0]
            queryset = Article.objects.filter(category=subcategory, status=AbstractStatus.PUBLISHED)
        else:
            queryset = CategoryArticle.objects.get(alias=catalog_slug).get_children().filter(status=AbstractStatus.PUBLISHED)
            if queryset:
                return queryset
            queryset = Article.objects.filter(category__alias=catalog_slug, status=AbstractStatus.PUBLISHED)
        return queryset

    def get_template_names(self):
        catalog_slug = self.kwargs.setdefault('catalog_alias', None)
        subcatalog_slug = self.kwargs.setdefault('subcatalog_alias', None)
        if not subcatalog_slug:
            queryset = CategoryArticle.objects.filter(alias=catalog_slug)[0].get_children().filter(status=AbstractStatus.PUBLISHED)
            if queryset.count():
                return ['article/category_list.html']
        return ['article/course_list.html']

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        subcatalog_slug = self.kwargs.setdefault('subcatalog_alias', None)
        catalog_slug = self.kwargs.setdefault('catalog_alias', None)
        context['catalog'] = CategoryArticle.objects.filter(alias=catalog_slug)[0]
        if subcatalog_slug:
            context['subcatalog'] = CategoryArticle.objects.filter(alias=subcatalog_slug)[0]
            context['meta'] = context['subcatalog'].as_meta(self.request)
        else:
            context['meta'] = context['catalog'].as_meta(self.request)
        return context


class ArticleListView(ShowOnlyPublishedView, ListView):
    template_name = 'article/article_list.html'
    model = Article
    context_object_name = 'article_list'
    paginate_by = 12

    def get_queryset(self):
        queryset = self.model.objects.filter(category__alias='blog', status=self.model.PUBLISHED)
        return queryset
