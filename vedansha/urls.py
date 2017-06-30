from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from homepage.views import HomePage
from article.views import CourseDetail, CategoryList

urlpatterns = [
    # Urls for Admin
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')),
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),

    # Urls for Site

    url(r'^$', HomePage.as_view(), name='home'),
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
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)