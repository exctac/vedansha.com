from django.conf.urls import url, include, handler404
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from homepage.views import HomePage
from article.views import ArticleDetail

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
    url(r'^', include('single_pages.urls')),
    url(r'^(?P<alias>[-\w]+)/$', ArticleDetail.as_view(), name='article'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)