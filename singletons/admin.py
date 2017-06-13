from django.contrib import admin
from solo.admin import SingletonModelAdmin
from singletons.models import *


class ListIconsItemInline(admin.StackedInline):
    model = ListIconsItem
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                ('status', 'icon', 'color'),
                'title',
                'text',
            )
        }),
    )


class YogaAllianceImagesInline(admin.StackedInline):
    model = YogaAllianceImages
    extra = 0


class PaymentMethodsImagesInline(admin.StackedInline):
    model = PaymentMethodsImages
    extra = 0


@admin.register(ListIcons)
class ListIconsAdmin(SingletonModelAdmin):
    inlines = [
        ListIconsItemInline
    ]


@admin.register(YogaAlliance)
class YogaAllianceAdmin(SingletonModelAdmin):
    inlines = [
        YogaAllianceImagesInline
    ]


@admin.register(PaymentMethods)
class PaymentMethodsAdmin(SingletonModelAdmin):
    inlines = [
        PaymentMethodsImagesInline
    ]


@admin.register(Copyright)
class CopyrightAdmin(SingletonModelAdmin):
    pass