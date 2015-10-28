# coding=utf-8
from django.conf.urls import patterns, url

__author__ = 'alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^robots\.txt', 'get_robots_txt', name='robots'),
)
