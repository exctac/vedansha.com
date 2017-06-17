from django.db import models
from solo.models import SingletonModel
from article.models import Article
from icons.models import IconGroup


class Contacts(SingletonModel):
    title = models.CharField("Title", max_length=255, blank=True, null=True, default="Contacts")
    subtitle = models.CharField("Subtitle", max_length=255, blank=True, null=True)
    address = models.CharField("Address", max_length=255, blank=True, null=True)
    email = models.CharField("Email", max_length=255, blank=True, null=True)
    phone_1 = models.CharField("Phone number first", max_length=255, blank=True, null=True)
    phone_2 = models.CharField("Phone number second", max_length=255, blank=True, null=True)
    icons_group = models.ForeignKey(
        IconGroup,
        verbose_name="Select group icons",
        help_text="If groups of icons are not created then create them",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
