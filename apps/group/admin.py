# coding=utf-8
from django.contrib import admin
from .models import Group,  GroupComment, GroupSection, GroupBanner

__author__ = 'alexy'


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'reserved', 'type', 'seats', 'price', 'travel_start', 'travel_end', 'pic']
    filter_horizontal = ['groupsection',]
    list_filter = ('type', 'groupsection', )
    prepopulated_fields = {'slug': ('title',)}


class GroupCommentAdmin(admin.ModelAdmin):
    list_display = ('group', 'user', 'created')

admin.site.register(Group, GroupAdmin)
admin.site.register(GroupSection)
admin.site.register(GroupComment, GroupCommentAdmin)
admin.site.register(GroupBanner)
