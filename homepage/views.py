from django.views.generic import TemplateView
from slider.models import Slider
from testimonials.models import Testimonials
from singletons.models import ListIcons, YogaAlliance, PaymentMethods, Copyright
from icons.models import IconGroup
from article.models import Article
from django.core.exceptions import ObjectDoesNotExist


class HomePage(TemplateView):
    template_name = "homepage/homepage.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['testimonials'] = Testimonials.objects.filter(status=Testimonials.PUBLISHED)[:3]
        context['yoga_alliance'] = YogaAlliance.get_solo()
        context['payment_methods'] = PaymentMethods.get_solo()
        context['list_icons'] = ListIcons.get_solo().get_items
        context['copyright'] = Copyright.get_solo()

        try:
            context['article'] = Article.objects.get(alias="dr-sanjeev-k-pandey", status=Article.PUBLISHED)
        except ObjectDoesNotExist:
            context['article'] = None

        try:
            context['footer_icons'] = IconGroup.objects.get(alias='footer-icons', status=IconGroup.PUBLISHED).get_icons
        except ObjectDoesNotExist:
            context['footer_icons'] = None

        try:
            context['slider'] = Slider.objects.filter(status=Slider.PUBLISHED, alias='offer-slider')
        except ObjectDoesNotExist:
            context['slider'] = None
        return context
