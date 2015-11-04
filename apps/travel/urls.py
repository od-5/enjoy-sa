# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from core.base_view import ExtraListView
from core.models import User
from .models import Travel
from .views import TravelCreateView

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^$', ExtraListView.as_view(
        model=Travel,
        extra_context={
            'author_list': User.objects.filter(first_name__isnull=False, last_name__isnull=False).exclude(avatar='')}),
        name='list'
        ),
    url(r'^add/$', TravelCreateView.as_view(), name='add'),
    url(r'^(?P<slug>[\w-]+)$', DetailView.as_view(model=Travel), name='detail'),
)
