from icons.models import IconGroup
from singletons.models import Copyright
from vedansha import settings


def footer_content(request):
    icons = IconGroup.objects.get(alias='footer-icons', status=IconGroup.PUBLISHED).get_icons
    return {
        'footer_icons': icons,
        'copyright': Copyright.get_solo()
    }


def get_settings(request):
    return {
        'GA': settings.GA,
    }
