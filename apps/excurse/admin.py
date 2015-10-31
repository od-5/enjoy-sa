# coding=utf-8
from django.contrib import admin
from .models import ExcurseSection, Excurse, ExcursePhoto


class ExcurseSectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ExcursePhotoInline(admin.TabularInline):
    model = ExcursePhoto
    extra = 1


class ExcurceAdmin(admin.ModelAdmin):
    inlines = (ExcursePhotoInline,)
    list_display = ['title', 'price', 'time', 'start', 'pic']


admin.site.register(ExcurseSection, ExcurseSectionAdmin)
admin.site.register(Excurse, ExcurceAdmin)
