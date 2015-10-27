# coding=utf-8
from django.db import models


__author__ = 'alexey'


class Common(models.Model):
    class Meta:
        abstract = True
        ordering = ['-created', ]

    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)


class CommonPage(Common):
    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=256, verbose_name=u'Заголовок')
    meta_title = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META заголовок')
    meta_key = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META ключевые слова')
    meta_desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=u'META описание')
