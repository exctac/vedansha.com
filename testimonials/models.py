from django.db import models
from common.models import AbstractStatus


class Testimonials(AbstractStatus):
    """
    Testimonials
    """
    title = models.CharField("Title", max_length=255)
    text = models.TextField("Text")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

