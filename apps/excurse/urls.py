# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView, ListView, DetailView
from .views import ExcurseListView, ExcurseDetailView
from .models import Excurse

__author__ = 'alexy'


urlpatterns = patterns(
    '',
    url(r'^$', ExcurseListView.as_view(), name='list'),
    url(r'^comment/$', 'apps.excurse.views.comment', name='comment'),
    url(r'^(?P<slug>[\w-]+)$', ExcurseDetailView.as_view(), name='detail'),
    # url(r'^', ListView.as_view(template_name='excurse/excurse_list.html'), name='list'),
)
