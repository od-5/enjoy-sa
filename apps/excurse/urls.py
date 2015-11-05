# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
from .views import ExcurseListView
from .models import Excurse

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ExcurseListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)$', DetailView.as_view(model=Excurse), name='detail'),
    # url(r'^', ListView.as_view(template_name='excurse/excurse_list.html'), name='list'),
)
