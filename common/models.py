from django.db import models


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

    def is_publish(self):
        if self.status == self.PUBLISHED:
            return True
        return False

# class AbstractIcons(models.Model):
#     """
#     Abstract model, adding the select field from choices status publish
#     """
#     PUBLISHED = 'p'
#     UNPUBLISHED = 'u'
#
#     CHOICES_STATUS = (
#         (PUBLISHED, '1'),
#         (UNPUBLISHED, '0')
#     )
#
#     icons = models.CharField("Icons", choices=CHOICES_STATUS, max_length=255, default=UNPUBLISHED, help_text="Select a status publish.")
#
#     def __unicode__(self):
#         return u"Status (abstract model)"
#
#     class Meta:
#         abstract = True
