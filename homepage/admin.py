from django.contrib import admin
from sitetree.admin import TreeItemAdmin, TreeAdmin, override_tree_admin, override_item_admin


class CustomTreeAdmin(TreeAdmin):
    list_display = ('title', 'alias')

override_tree_admin(CustomTreeAdmin)
