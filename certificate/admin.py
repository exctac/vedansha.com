from django.contrib import admin
from certificate.models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title']
    fields = (
        'title',
        ('image', 'image_alt',),
        'text',
    )