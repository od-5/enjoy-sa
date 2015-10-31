# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView
from .models import Faq

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=Faq), name='list'),
)
