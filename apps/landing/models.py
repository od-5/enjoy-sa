# coding=utf-8
import os
import uuid
from django.conf import settings
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize

from core.base_model import Common

__author__ = 'alexy'


def get_image_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('why', filename)

def get_doc_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('document', filename)

def get_photo_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('photo', filename)

def get_review_path(self, filename):
    extension = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), extension)
    return os.path.join('review', filename)


class Why(models.Model):
    class Meta:
        verbose_name = u'Почему именно мы'
        verbose_name_plural = u'Почему именно мы'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.icon_resize.url

    pic.short_description = u"Иконка"
    pic.allow_tags = True

    name = models.CharField(verbose_name=u'Заголовок', max_length=256)
    text = models.TextField(verbose_name=u'Текст')
    icon = models.ImageField(upload_to=get_image_path, verbose_name=u'Иконка')
    icon_resize = ImageSpecField(
        [SmartResize(*settings.WHY_ICON_SIZE)], source='icon', format='PNG', options={'quality': 94}
    )


class Document(models.Model):
    class Meta:
        verbose_name = u'Наши документы'
        verbose_name_plural = u'Наши документы'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url

    pic.short_description = u"Изображение"
    pic.allow_tags = True

    name = models.CharField(verbose_name=u'Название', max_length=256)
    image = models.ImageField(upload_to=get_doc_path, verbose_name=u'Изображение')
    image_resize = ImageSpecField(
        [SmartResize(*settings.DOC_IMAGE_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )


class Photo(models.Model):
    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url

    pic.short_description = u"Изображение"
    pic.allow_tags = True

    name = models.CharField(verbose_name=u'Название', max_length=256)
    image = models.ImageField(upload_to=get_photo_path, verbose_name=u'Изображение')
    image_resize = ImageSpecField(
        [SmartResize(*settings.PHOTO_IMAGE_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )


class Why2(models.Model):
    class Meta:
        verbose_name = u'Почему выбирают именно нас'
        verbose_name_plural = u'Почему выбирают именно нас'
        app_label = 'landing'

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')


class Review(models.Model):
    class Meta:
        verbose_name = u'Впечатления от поездок'
        verbose_name_plural = u'Впечатления от поездок'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def pic(self):
        return '<img src="%s" width="170"/>' % self.photo_resize.url

    pic.short_description = u"Фотография"
    pic.allow_tags = True

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    text = models.TextField(verbose_name=u'Текст')
    photo = models.ImageField(upload_to=get_review_path, verbose_name=u'Фотография')
    photo_resize = ImageSpecField(
        [SmartResize(*settings.REVIEW_PHOTO_SIZE)], source='photo', format='JPEG', options={'quality': 94}
    )
