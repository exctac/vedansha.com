from django.views.generic import ListView
from certificate.models import Certificate
from common.views import ShowOnlyPublishedView


class CertificateListView(ShowOnlyPublishedView, ListView):
    template_name = 'certificate/certificates.html'
    model = Certificate
    context_object_name = 'certificates'
