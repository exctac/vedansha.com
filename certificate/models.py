from django.db import models
from common.models import AbstractStatus, AbstractMeta


class Certificate(AbstractStatus):
    """
    Certificate
    """
    title = models.CharField("Title", max_length=255)
    image = models.ImageField("Image", upload_to="certificates_images")
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)
    text = models.TextField("Text", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
