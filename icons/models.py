from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify

from common.models import AbstractStatus


class Icon(AbstractStatus):
    ICONS_CHOICES = (
        ('google-plus', 'google-plus'),
        ('google-wallet', 'google-wallet'),
        ('pinterest', 'pinterest'),
        ('facebook', 'facebook'),
        ('odnoklassniki', 'odnoklassniki'),
        ('telegram', 'telegram'),
        ('twitter', 'twitter'),
        ('skype', 'skype'),
        ('tumblr', 'tumblr'),
        ('youtube', 'youtube'),
        ('instagram', 'instagram'),
        ('linkedin', 'linkedin'),
        ('vimeo', 'vimeo'),
        ('vk', 'vk'),
        ('booking', 'booking'),
        ('tripadvisor', 'tripadvisor'),
        ('book', 'book'),
        ('clear-sun', 'samopoznanie'),
    )
    name = models.CharField(
        "Icon name",
        max_length=255,
        blank=True,
        default=None,
        help_text="Leave this field blank, a name will be generated automatically"
    )
    icons = models.CharField(
        "Select icon",
        choices=ICONS_CHOICES,
        max_length=255,
        help_text="Select an icon from the list"
    )
    url = models.CharField(
        "Url",
        max_length=255,
        blank=True,
        default=None,
        help_text="If you want that icon was a link to enter the website address"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Icon"
        verbose_name_plural = "Icons"

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.icons.title()
        super(Icon, self).save(*args, **kwargs)


class IconGroup(AbstractStatus):
    name = models.CharField("Group name", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True, default=None)
    icons = models.ManyToManyField(Icon, verbose_name="Select icons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Group icons"
        verbose_name_plural = "Group icons"

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = slugify(self.name)
        super(IconGroup, self).save(*args, **kwargs)

    @property
    def get_icons(self):
        return self.icons.all()
