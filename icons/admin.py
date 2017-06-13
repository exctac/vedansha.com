from django.contrib import admin
from icons.models import Icon, IconGroup


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_editable = ('status',)


@admin.register(IconGroup)
class IconGroupAdmin(admin.ModelAdmin):
    fields = ['status', 'name', 'alias', 'icons']
    filter_horizontal = ('icons',)
    list_display = ('name', 'status')
    readonly_fields = ['alias']
    list_editable = ('status',)
