from django.db import models

from common.models import AbstractStatus


class Faq(AbstractStatus):
    question = models.CharField('Question', max_length=255)
    answer = models.TextField('Answer')

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
