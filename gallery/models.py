import os

import itertools
from django.db import models
from django.utils.text import slugify
from easy_thumbnails.fields import ThumbnailerImageField
from easy_thumbnails.files import get_thumbnailer
from solo.models import SingletonModel
from common.models import AbstractStatus, AbstractMeta
from vedansha import settings


class PhotoGallery(AbstractStatus, AbstractMeta):
    title = models.CharField("Title", max_length=255)
    alias = models.CharField("Alias", max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Photo gallery"
        verbose_name_plural = "Photo galleries"

    @property
    def get_preview_image(self):
        """
        Get preview image
        """
        image = self.photo_set.first()
        default_image = None
        if not image:
            default_image = get_thumbnailer('no_image.png')
        return default_image or image.image


    @property
    def get_all_images(self):
        """
        Get all images generator
        """
        all_images = (image for image in self.photo_set.all())
        return all_images

    def save(self, *args, **kwargs):
        if not self.alias:
            orig = self.alias = slugify(self.title)
            for x in itertools.count(1):
                if not PhotoGallery.objects.filter(alias=self.alias).exists():
                    break
                self.alias = '%s-%d' % (orig, x)
        super(PhotoGallery, self).save(*args, **kwargs)


class Photo(models.Model):
    gallery = models.ForeignKey(PhotoGallery)
    image = ThumbnailerImageField(
        "Image",
        upload_to='photo_gallery/',
        help_text="Add photo to the photo gallery"
    )
    image_alt = models.CharField('Image alternative text', max_length=255, blank=True, null=True)


class VideoGallery(SingletonModel, AbstractMeta):
    """ 
    Video Gallery
    """

    def __str__(self):
        return u"Video Gallery"

    def get_videos(self):
        """
        Get all videos links generator
        :return: all_videos generator
        """
        all_videos = (image for image in self.videogallerylink_set.filter(status=AbstractStatus.PUBLISHED))
        return all_videos


class VideoGalleryLink(AbstractStatus):
    """
    Video Gallery link an video
    """
    video_code = models.CharField(
        "Video code",
        max_length=255,
        blank=True,
        null=True,
        help_text="Paste in this field youtube video's code. For example: https://youtu.be/<strong>ZiC8ZSKKXwU</strong>"
    )
    parent = models.ForeignKey(VideoGallery)
