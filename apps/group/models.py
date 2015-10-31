# coding=utf-8
import os
import uuid
from ckeditor.fields import RichTextField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from pytils.translit import slugify
from core.base_model import Common, CommonPage

__author__ = 'alexy'

def get_image_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('group', filename)


class Group(CommonPage):
    class Meta:
        verbose_name = u'Групповой тур'
        verbose_name_plural = u'Групповые туры'
        app_label = 'group'
        ordering = ['-travel_start']

    def __unicode__(self):
        return u'Тур %s, с %s по %s' % (self.title, self.travel_start, self.travel_end)

    def save(self):
        self.slug = slugify(self.title)
        super(Group, self).save()

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'slug': self.slug})

    def pic(self):
        return '<img src="%s" width="170"/>' % self.cover_resize.url

    pic.short_description = u"Обложка"
    pic.allow_tags = True

    description = RichTextField(verbose_name=u'Описание', blank=True, null=True)
    reserved = models.PositiveIntegerField(verbose_name=u'Забронировано мест', default=0)
    seats = models.PositiveIntegerField(verbose_name=u'Количество мест', default=0)
    price = models.PositiveIntegerField(verbose_name=u'Стоимость', default=0)
    cover = models.ImageField(verbose_name=u'Обложка', upload_to=get_image_path)
    cover_resize = ImageSpecField(
        [SmartResize(*settings.GROUP_COVER_SIZE)], source='cover', format='JPEG', options={'quality': 94}
    )
    travel_start = models.DateField(verbose_name=u'Прибытие', blank=True, null=True)
    travel_end = models.DateField(verbose_name=u'Отъезд', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)
