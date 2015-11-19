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
from core.base_model import Common, CommonPage, Comment

__author__ = 'alexy'

def get_image_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('group', filename)


class GroupSection(models.Model):
    class Meta:
        verbose_name = u'Направление'
        verbose_name_plural = u'Направления'
        app_label = 'group'

    def __unicode__(self):
        return self.name

    name = models.CharField(verbose_name=u'Название', max_length=250)


class Group(CommonPage):
    class Meta:
        verbose_name = u'Наш тур'
        verbose_name_plural = u'Наши туры'
        app_label = 'group'
        ordering = ['-created', ]

    def __unicode__(self):
        return u'Тур %s, с %s по %s' % (self.title, self.travel_start, self.travel_end)

    def save(self):
        self.slug = slugify(self.title)
        delta = self.travel_end - self.travel_start
        self.day_count = delta.days
        super(Group, self).save()

    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'slug': self.slug})

    def pic(self):
        return '<img src="%s" width="170"/>' % self.cover_resize.url

    pic.short_description = u"Обложка"
    pic.allow_tags = True

    groupsection = models.ManyToManyField(to=GroupSection, verbose_name=u'Направление', blank=True, null=True)
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
    day_count = models.PositiveIntegerField(default=0, verbose_name=u'Количество дней')


class GroupComment(Comment):
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'group'

    group = models.ForeignKey(to=Group, verbose_name=u'Тур')
