from django.conf.urls import url
from certificate.views import CertificateListView

urlpatterns = [
    url(r'^$', CertificateListView.as_view(), name='certificates_list'),
]