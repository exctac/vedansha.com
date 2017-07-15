from django.contrib import admin
from solo.admin import SingletonModelAdmin
from single_pages.models import *


@admin.register(Contacts)
class ContactsAdmin(SingletonModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'subtitle',
                'address',
                'email',
                'phone_1',
                'phone_2',
                'icons_group',
            )
        }),
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(Members)
class MembersAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(Certificates)
class CertificatesAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(TestimonialsPage)
class TestimonialsPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(HomePage)
class HomePageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(BookingPage)
class BookingPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )


@admin.register(PhotoGalleriesPage)
class PhotoGalleriesPageAdmin(SingletonModelAdmin):
    fieldsets = (
        ('META options', {
            'classes': ('collapse',),
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
        }),
    )

