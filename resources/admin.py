from django.contrib import admin
from resources.models import BookCategory, Book


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    list_editable = ['category']
