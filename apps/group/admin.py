# coding=utf-8
from django.contrib import admin
from .models import Group

__author__ = 'alexy'


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'reserved', 'seats', 'price', 'travel_start', 'travel_end', 'pic']


admin.site.register(Group, GroupAdmin)
