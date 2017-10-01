from django.conf.urls import url, include
from django.contrib import admin
# from django.conf import settings
from django.shortcuts import render_to_response

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from homepage.views import Home
from article.views import CourseDetail, CategoryList
from vedansha import settings
from vedansha.views import SitemapView, UrlListView, GoogleSiteVerificationView

urlpatterns = [
    # Urls for Admin
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')),
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    # Urls for Site

    url(r'^$', Home.as_view(), name='home'),
    url(r'^sitemap.xml/$', SitemapView.as_view(), name='sitemap'),
    url(r'^urllist.txt/$', UrlListView.as_view(), name='urllist'),
    url(r'^googleea1438b485c8eb7f.html/$', GoogleSiteVerificationView.as_view(), name='google_verify'),
    url(r'^faq/', include('faq.urls'), name='faq'),
    url(r'^testimonials/', include('testimonials.urls'), name='testimonials'),
    url(r'^certificates/', include('certificate.urls'), name='certificates'),
    url(r'^news/', include('news.urls'), name='news'),
    url(r'^', include('single_pages.urls'), name='single_pages'),
    url(r'^', include('gallery.urls'), name='gallery'),
    url(r'^', include('team.urls'), name='team'),
    # courses, this is will be change
    url(r'^courses/(?P<catalog_alias>[-\w]+)/$', CategoryList.as_view(), name='courses_catalog'),
    url(r'^courses/(?P<catalog_alias>[-\w]+)/(?P<subcatalog_alias>[-\w]+)/$', CategoryList.as_view(), name='courses_subcatalog'),
    url(r'^course/(?P<alias>[-\w]+)/$', CourseDetail.as_view(), name='course_detail'),
] + [
    # for article page
    url(r'^', include('article.urls'), name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()