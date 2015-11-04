# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from core.views import UserUpdateView

__author__ = 'alexy'


urlpatterns = patterns(
    'core.views',
    url(r'^robots\.txt', 'get_robots_txt', name='robots'),
    url(r'^profile/$', UserUpdateView.as_view(), name='profile'),
    url(r'^accounts/login/$', 'landing_login', name='login'),
    url(r'^accounts/registration/$', 'landing_registration', name='registration'),
)
