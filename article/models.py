from django.db import models
from django.utils.text import slugify

from common.models import AbstractStatus
from icons.models import IconGroup


class Article(AbstractStatus):
    create_date = models.DateTimeField("Create date", auto_now=True)
    show_date = models.BooleanField("Show create date", default=True)
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    image = models.ImageField(
        "Image",
        upload_to='articles/',
        blank=True,
        help_text="Main picture of the article (optional field)"
    )
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
            self.alias = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_image(self):
        pass
