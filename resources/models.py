import itertools
from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer

from common.models import AbstractStatus


class BookCategory(AbstractStatus):
    title = models.CharField('Category title', max_length=255)
    alias = models.CharField("Alias", max_length=255, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book Category"
        verbose_name_plural = "Book Categories"

    def get_books(self):
        return self.book.filter(status=AbstractStatus.PUBLISHED)

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not BookCategory.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(BookCategory, self).save(*args, **kwargs)


class Book(AbstractStatus):
    title = models.CharField('Book title', max_length=255)
    author = models.CharField('Book Author', max_length=255, blank=True, null=True)
    alias = models.CharField("Alias", max_length=255, editable=False)
    category = models.ForeignKey(BookCategory, related_name='book')
    image = ThumbnailerImageField(
        "Image",
        upload_to='books/',
        blank=True,
        null=True,
        help_text="Main picture of the Book (optional field)"
    )
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)
    show_image = models.BooleanField("Show image?", default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def get_image(self):
        image = self.image
        default_image = None
        if not image:
            default_image = get_thumbnailer('no_image.png')
        return default_image or image

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not Book.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(Book, self).save(*args, **kwargs)