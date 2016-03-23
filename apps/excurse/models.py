# coding=utf-8
import os
import uuid
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from pytils.translit import slugify
from core.base_model import CommonPage, Comment

__author__ = 'alexy'

def get_image_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('excurse', filename)


class ExcurseSection(models.Model):
    class Meta:
        verbose_name = u'Направление'
        verbose_name_plural = u'Направления'
        app_label = 'excurse'

    def __unicode__(self):
        return self.name

    name = models.CharField(verbose_name=u'Название', max_length=250)


class Excurse(CommonPage):
    class Meta:
        verbose_name = u'Экскурсия'
        verbose_name_plural = u'Экскурсии'
        app_label = 'excurse'
        ordering = ['-created', ]

    def __unicode__(self):
        return self.title

    # def save(self):
    #     self.slug = slugify(self.title)
    #     super(Excurse, self).save()

    def pic(self):
        return '<img src="%s" width="170"/>' % self.cover_resize.url

    def get_absolute_url(self):
        return reverse('excurse:detail', kwargs={'slug': self.slug})

    pic.short_description = u"Обложка"
    pic.allow_tags = True

    section = models.ForeignKey(to=ExcurseSection, verbose_name=u'Направление')
    # name = models.CharField(verbose_name=u'Название', max_length=250)
    cover = models.ImageField(upload_to=get_image_path, verbose_name=u'Обложка')
    cover_resize = ImageSpecField(
        [SmartResize(*settings.EXCURSE_COVER_SIZE)], source='cover', format='JPEG', options={'quality': 94}
    )
    price = models.PositiveIntegerField(verbose_name=u'Стоимость', blank=True, null=True)
    price_desc = models.TextField(verbose_name=u'Описание стоимости', blank=True, null=True)
    time = models.CharField(verbose_name=u'Длительность', max_length=250, blank=True, null=True)
    start = models.CharField(verbose_name=u'Отправка', max_length=250, blank=True, null=True)
    text = RichTextField(verbose_name=u'Текст')
    slug = models.SlugField(max_length=100, verbose_name=u'url')


class ExcursePhoto(models.Model):
    class Meta:
        verbose_name = u'Фотография с экскурсии'
        verbose_name_plural = u'Фотографии с экскурсии'
        app_label = 'excurse'

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url

    pic.short_description = u"Обложка"
    pic.allow_tags = True

    excurse = models.ForeignKey(to=Excurse, verbose_name=u'Экскурсия')
    name = models.CharField(verbose_name=u'Название', max_length=250)
    image = models.ImageField(upload_to=get_image_path, verbose_name=u'Фотография')
    image_resize = ImageSpecField(
        [SmartResize(*settings.EXCURSE_COVER_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )


class ExcurseComment(Comment):
    class Meta:
        verbose_name = u'Комментарий'
        verbose_name_plural = u'Комментарии'
        app_label = 'excurse'

    excurse = models.ForeignKey(to=Excurse, verbose_name=u'Экскурсия')
