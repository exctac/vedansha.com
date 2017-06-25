import os
import itertools
from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from common.models import AbstractStatus
from vedansha import settings


class Member(AbstractStatus):
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    image = ThumbnailerImageField(
        "Image",
        upload_to='team/',
        # blank=True,
        help_text="Main picture of the Team (optional field)"
    )
    show_image = models.BooleanField("Show image?", default=True, editable=False)
    text = models.TextField("Text", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not Member.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(Member, self).save(*args, **kwargs)

    @property
    def get_image(self):
        """
        Get Member image
        """
        image = self.image
        if not image:
            image = get_thumbnailer(open(settings.NO_AVATAR), relative_name="img/no_avatar.jpg")
        return image