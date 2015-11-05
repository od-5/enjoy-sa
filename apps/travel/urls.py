# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import DetailView
from .models import Travel
from .views import TravelCreateView, TravelListView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^$', TravelListView.as_view(), name='list'),
    url(r'^add/$', TravelCreateView.as_view(), name='add'),
    url(r'^(?P<slug>[\w-]+)$', DetailView.as_view(model=Travel), name='detail'),
)
