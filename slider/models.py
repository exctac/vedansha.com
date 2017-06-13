from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from common.models import AbstractStatus
from django.utils.text import slugify


class Slider(AbstractStatus):
    """
    Contents or images slider
    """
    name = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"

    @property
    def get_slides(self):
        """
        Get Slides for Slider
        :return: slides objects or None
        """
        slides = self.slide_set.filter(status=self.PUBLISHED)
        if slides:
            return slides
        return None

    def save(self, *args, **kwargs):
        if not self.alias:
            self.alias = slugify(self.name)
        super(Slider, self).save(*args, **kwargs)


class Slide(AbstractStatus):
    """
    The associated model from Slider
    """
    slider = models.ForeignKey(Slider)
    title = models.CharField("Title", max_length=255, blank=True)
    text = models.TextField("Text", blank=True)
    image = ThumbnailerImageField("Image", upload_to="slider", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slide"
        verbose_name_plural = "Slides"

