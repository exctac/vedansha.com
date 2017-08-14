from icons.models import IconGroup
from singletons.models import Copyright
from vedansha import settings
from singletons.models import FloatIconBlock


def footer_content(request):
    icons = IconGroup.objects.filter(alias='footer-icons', status=IconGroup.PUBLISHED)[0].get_icons
    return {
        'footer_icons': icons,
        'copyright': Copyright.get_solo()
    }


def float_icons(request):
    icons = FloatIconBlock.get_solo().icons_group.get_icons
    return {
        'float_icons': icons
    }


def get_settings(request):
    return {
        'GA': settings.GA,
    }
