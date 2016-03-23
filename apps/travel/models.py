# -*- coding: utf-8 -*-
import os
import uuid
from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from pytils.translit import slugify
from core.base_model import Common, CommonPage, Comment
from core.models import User

__author__ = 'alexy'


def get_image_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('travel', filename)


class Travel(CommonPage):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'travel'

    def __unicode__(self):
        return self.title
    #
    # def save(self):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super(Travel, self).save()

    def get_absolute_url(self):
        return reverse('travels:detail', kwargs={'slug': self.slug})

    def pic(self):
        return '<img src="%s" width="170"/>' % self.cover_resize.url

    pic.short_description = u"Обложка"
    pic.allow_tags = True

    user = models.ForeignKey(to=User, verbose_name=u'Пользователь')
    # title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    text = RichTextField(verbose_name=u'Текст')
    cover = models.ImageField(verbose_name=u'Обложка', upload_to=get_image_path)
    cover_resize = ImageSpecField(
        [SmartResize(*settings.TRAVEL_COVER_SIZE)], source='cover', format='JPEG', options={'quality': 94}
    )
    slug = models.SlugField(max_length=100, verbose_name=u'url')


class TravelComment(Comment):
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'travel'

    travel = models.ForeignKey(to=Travel, verbose_name=u'Статья')