# coding=utf-8
from django.contrib import admin
from .models import About

__author__ = 'alexy'


class AboutAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(About, AboutAdmin)
