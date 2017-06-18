from django.db import models
from common.models import AbstractStatus


class Certificate(AbstractStatus):
    """
    Certificate
    """
    title = models.CharField("Title", max_length=255)
    image = models.ImageField("Image", upload_to="certificates_images")
    text = models.TextField("Text", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
