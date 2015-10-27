# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^', TemplateView.as_view(template_name='travel/travel_list.html'), name='list'),
)
