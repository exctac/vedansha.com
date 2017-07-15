from django.db import models
from meta.models import ModelMeta


class AbstractStatus(models.Model):
    """
    Abstract model, adding the select field from choices status publish  
    """
    PUBLISHED = 'p'
    UNPUBLISHED = 'u'
    CHOICES_STATUS = (
        (PUBLISHED, "Published"),
        (UNPUBLISHED, "Unpublished")
    )

    status = models.CharField("Status", choices=CHOICES_STATUS, max_length=1, default=UNPUBLISHED, help_text="Select a status publish.")

    class Meta:
        abstract = True

    @property
    def is_publish(self):
        if self.status == self.PUBLISHED:
            return True
        return False


class AbstractMeta(ModelMeta, models.Model):
    meta_title = models.CharField("Title", max_length=255, blank=True)
    meta_description = models.TextField("Description", blank=True)
    meta_keywords = models.TextField(
        "Keywords",
        blank=True,
        help_text='Keywords are written comma-separated, for example "word 1, word 2, word 3, ..."'
    )
    _metadata = {
        'title': 'meta_title',
        'description': 'meta_description',
        'keywords': 'get_meta_keywords',
    }

    @property
    def get_meta_keywords(self):
        if self.meta_keywords:
            return [kw.strip() for kw in self.meta_keywords.split(',')]
        return ''

    class Meta:
        abstract = True
