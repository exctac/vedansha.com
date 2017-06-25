import os
import itertools
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from mptt.models import MPTTModel, TreeForeignKey
from common.models import AbstractStatus
from icons.models import IconGroup
from vedansha import settings
import mptt


class CategoryArticle(MPTTModel, AbstractStatus):
    title = models.CharField("Title", max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Category")
    alias = models.CharField("Alias", max_length=255, blank=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='articles/',
        # blank=True,
        help_text="Main picture of the article (optional field)"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_image(self):
        """
        Get Category image
        """
        image = self.image
        if not image:
            image = get_thumbnailer(open(settings.NO_AVATAR), relative_name='no_image.png')
        return image

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not Article.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(CategoryArticle, self).save(*args, **kwargs)


mptt.register(CategoryArticle)


class Article(AbstractStatus):
    create_date = models.DateTimeField("Create date", default=timezone.now, blank=True)
    show_date = models.BooleanField("Show create date?", default=True)
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    category = models.ForeignKey(CategoryArticle, verbose_name=u"Category", null=True, blank=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='articles/',
        # blank=True,
        help_text="Main picture of the article (optional field)"
    )
    show_image = models.BooleanField("Show image?", default=True)
    text = models.TextField("Text", blank=True)
    icons_group = models.ForeignKey(
        IconGroup,
        verbose_name="Select group icons",
        help_text="If groups of icons are not created then create them",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not Article.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(Article, self).save(*args, **kwargs)

    def get_image(self):
        """
        Get Article image
        """
        image = self.image
        if not image:
            image = get_thumbnailer(open(settings.NO_AVATAR), relative_name='no_image.png')
        return image


