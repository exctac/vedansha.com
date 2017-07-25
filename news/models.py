from django.db import models
from django.utils import timezone
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer

from common.models import AbstractStatus, AbstractMeta
from django.utils.text import slugify
from icons.models import IconGroup


class News(AbstractStatus, AbstractMeta):
    """
    News
    """
    create_date = models.DateTimeField("Create date", default=timezone.now, blank=True, null=True)
    show_date = models.BooleanField("Show create date", default=True)
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True, null=True)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True, null=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='news_images/',
        blank=True,
        null=True,
        help_text="Main picture of the news (optional field). This picture will by displayed in the news list"
    )
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)
    show_image = models.BooleanField("Show image?", default=True)
    text = models.TextField("Text", blank=True, null=True)
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
        verbose_name = "News"
        verbose_name_plural = "News list"

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = slugify(self.title)
        super(News, self).save(*args, **kwargs)

    def get_image(self):
        image = self.image
        default_image = None
        if not image:
            default_image = get_thumbnailer('no_image.png')
        return default_image or image
