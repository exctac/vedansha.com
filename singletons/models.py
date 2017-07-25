from django.db import models
from solo.models import SingletonModel
from common.models import AbstractStatus


class Copyright(SingletonModel):
    """ 
    Copyright text in footer
    """
    text = models.TextField("Copyright text", max_length=255, blank=False)

    def __str__(self):
        return u"Copyright model"

    class Meta:
        verbose_name = "Copyright"


class YogaAlliance(SingletonModel):
    """ 
    Yoga Alliance information
    """
    text = models.CharField("Text", max_length=255)
    url = models.CharField(
        "Url",
        max_length=255,
        blank=True,
        null=True,
        help_text="Add the url of the page if you want that the text field was a link"
    )

    def __str__(self):
        return u"Yoga Alliance information"

    def get_images(self):
        images = self.yogaallianceimages_set.all()
        if images:
            return images
        return None


class YogaAllianceImages(models.Model):
    """ 
    Yoga Alliance information images 
    """
    image = models.ImageField("Image", upload_to="yoga_alliance/")
    parent = models.ForeignKey(YogaAlliance)


class PaymentMethods(SingletonModel):
    """ 
    Payment methods information
    """
    text = models.CharField("Text", max_length=255)
    url = models.CharField(
        "Url",
        max_length=255,
        blank=True,
        null=True,
        default=None,
        help_text="Add the url of the page if you want that the text field was a link"
    )

    def __str__(self):
        return u"Payment methods information"

    def get_images(self):
        images = self.paymentmethodsimages_set.all()
        if images:
            return images
        return None


class PaymentMethodsImages(models.Model):
    """ 
    Payment methods images 
    """
    image = models.ImageField("Image", upload_to="payment_methods/")
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)
    parent = models.ForeignKey(PaymentMethods)


class ListIcons(SingletonModel):
    """ 
    ListIcons
    """

    @property
    def get_items(self):
        items = self.listiconsitem_set.all()
        if items:
            return items
        return None


class ListIconsItem(AbstractStatus):
    """ 
    Yoga Alliance information images 
    """
    CHOICES_COLORS = [
        ('gray-light', 'gray-light'),
        ('gray', 'gray'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('orange', 'orange'),
        ('blue ', 'blue '),
    ]
    CHOICES_ICONS = (
        ('lotus', 'Lotus'),
        ('om-symbol', 'Om symbol'),
        ('skype', 'Skype'),
        ('views', 'Views'),
        ('cube-questions-mark', 'Cube questions'),
        ('moon', 'Moon'),
    )
    title = models.CharField("Title", max_length=255, blank=False)
    icon = models.CharField("Icon", choices=CHOICES_ICONS, max_length=20, blank=True)
    color = models.CharField("Header color", choices=CHOICES_COLORS, max_length=20, blank=True, )
    text = models.TextField("Text", max_length=255, blank=False)
    parent = models.ForeignKey(ListIcons)

