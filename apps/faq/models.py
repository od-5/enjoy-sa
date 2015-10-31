# -*- coding: utf-8 -*-
import os
import uuid
from ckeditor.fields import RichTextField
from django.db import models
from pytils.translit import slugify

__author__ = 'alexy'


class Faq(models.Model):
    class Meta:
        verbose_name = u'Вопросы и ответы'
        verbose_name_plural = u'Вопросы и ответы'
        app_label = 'faq'

    def __unicode__(self):
        return self.question

    question = models.TextField(verbose_name=u'Вопрос')
    answer = RichTextField(verbose_name=u'Ответ')
