import os
import itertools
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from mptt.models import MPTTModel, TreeForeignKey
from common.models import AbstractStatus, AbstractMeta
from icons.models import IconGroup
import mptt


class CategoryArticle(MPTTModel, AbstractMeta, AbstractStatus):
    title = models.CharField("Title", max_length=255)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u"Category")
    alias = models.CharField("Alias", max_length=255, blank=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='articles/',
        blank=True,
        null=True,
        help_text="Main picture of the article (optional field)"
    )
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)

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
        default_image = None
        if not image:
            default_image = get_thumbnailer('no_image.png')
        return default_image or image

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not CategoryArticle.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(CategoryArticle, self).save(*args, **kwargs)


mptt.register(CategoryArticle)


class Article(AbstractStatus, AbstractMeta):
    show_homepage_help = "only one article can be displayed on the main page. " \
                              "If the checkbox is already installed on another article, " \
                              "the new checkbox will replace it."
    image_help = "Main picture of the article (optional field)"
    icons_group_help = "If groups of icons are not created then create them"

    create_date = models.DateTimeField("Create date", default=timezone.now, blank=True)
    show_date = models.BooleanField("Show create date?", default=True)
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    category = models.ForeignKey(CategoryArticle, verbose_name=u"Category", null=True, blank=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='articles/',
        blank=True,
        null=True,
        help_text=image_help
    )
    show_homepage = models.BooleanField("Show in index page?", default=False, help_text=show_homepage_help)
    show_image = models.BooleanField("Show image?", default=True)
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)
    text = models.TextField("Text", blank=True)
    icons_group = models.ForeignKey(
        IconGroup,
        verbose_name="Select group icons",
        help_text=icons_group_help,
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
        default_image = None
        if not image:
            default_image = get_thumbnailer('no_image.png')
        return default_image or image

