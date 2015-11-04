# coding=utf-8
from django.db import models
from core.base_model import CommonPage


__author__ = 'alexy'


class Page(CommonPage):
    class Meta:
        verbose_name = u'Страница'
        verbose_name_plural = u'Страницы'
        app_label = 'seo'

    PAGE_CHOICES = (
        ('home', u'Главная страница'),
        ('about', u'О нас'),
        ('travels', u'Журнал путешествий'),
        ('groups', u'Групповые туры'),
        ('excurse', u'Экскурсии'),
        ('faq', u'Вопросы и ответы'),
    )

    def __unicode__(self):
        return self.get_page_display()

    page = models.CharField(max_length=100, choices=PAGE_CHOICES, unique=True, verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст на странице', blank=True, null=True)
