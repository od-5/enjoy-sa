# coding=utf-8
from django.contrib import admin
from .models import Travel

__author__ = 'alexy'


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic')

admin.site.register(Travel, TravelAdmin)
