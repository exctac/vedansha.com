from django.views.generic import ListView
from certificate.models import Certificate
from common.views import ShowOnlyPublishedView
from single_pages.models import Certificates


class CertificateListView(ShowOnlyPublishedView, ListView):
    template_name = 'certificate/certificates.html'
    model = Certificate
    context_object_name = 'certificates'

    def get_context_data(self, **kwargs):
        context = super(CertificateListView, self).get_context_data(**kwargs)
        context['meta'] = Certificates.get_solo().as_meta(self.request)
        return context