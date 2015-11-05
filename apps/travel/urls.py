# coding=utf-8
from django.conf.urls import patterns, url
from .views import TravelCreateView, TravelListView, TravelDetailView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^$', TravelListView.as_view(), name='list'),
    url(r'^add/$', TravelCreateView.as_view(), name='add'),
    url(r'^comment/$', 'apps.travel.views.comment', name='comment'),
    url(r'^(?P<slug>[\w-]+)$', TravelDetailView.as_view(), name='detail'),
)
