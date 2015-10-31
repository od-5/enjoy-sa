# coding=utf-8
from django.contrib import admin
from .models import Faq

__author__ = 'alexy'


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)

admin.site.register(Faq, FaqAdmin)
