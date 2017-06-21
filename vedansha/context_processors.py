from icons.models import IconGroup
from singletons.models import Copyright


def footer_content(request):
    icons = IconGroup.objects.get(alias='footer-icons', status=IconGroup.PUBLISHED).get_icons
    return {
        'footer_icons': icons,
        'copyright': Copyright.get_solo()
    }
