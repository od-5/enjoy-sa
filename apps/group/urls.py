# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from apps.group.views import GroupDetailView
from .models import Group

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view(model=Group), name='list'),
    url(r'^comment/$', 'apps.group.views.comment', name='comment'),
    url(r'^(?P<slug>[\w-]+)$', GroupDetailView.as_view(), name='detail'),
)
