# coding=utf-8
from django.contrib import admin
from .models import Travel, TravelComment

__author__ = 'alexy'


class TravelAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic')
    prepopulated_fields = {'slug': ('title',)}


class TravelCommentAdmin(admin.ModelAdmin):
    list_display = ('travel', 'user', 'created')


admin.site.register(Travel, TravelAdmin)
admin.site.register(TravelComment, TravelCommentAdmin)
