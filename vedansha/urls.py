from django.conf.urls import url, include
from django.contrib import admin

from homepage.views import homepage

urlpatterns = [
    # Urls for Admin
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    # Urls for Site
    url(r'^$', homepage, name='home'),
]
