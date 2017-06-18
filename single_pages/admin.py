from django.contrib import admin
from solo.admin import SingletonModelAdmin
from single_pages.models import *


@admin.register(Contacts)
class ContactsAdmin(SingletonModelAdmin):
    pass

