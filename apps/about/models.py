# -*- coding: utf-8 -*-
import os
import uuid
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse
from django.db import models
from pytils.translit import slugify

__author__ = 'alexy'


class About(models.Model):
    class Meta:
        verbose_name = u'О нас'
        verbose_name_plural = u'О нас'
        app_label = 'about'

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(About, self).save()

    title = models.CharField(verbose_name=u'Заголовок', max_length=255)
    text = RichTextField(verbose_name=u'Текст')
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)
