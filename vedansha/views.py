from django.views.generic import TemplateView


class SitemapView(TemplateView):
    content_type = 'application/xml'
    template_name = 'vedansha/sitemap.xml'


class UrlListView(TemplateView):
    content_type = 'text/html'
    template_name = 'vedansha/urllist.txt'


class GoogleSiteVerificationView(TemplateView):
    template_name = 'vedansha/googleea1438b485c8eb7f.html'