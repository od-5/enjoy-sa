# coding=utf-8
from django.contrib import admin
from .models import Why, Document, Photo, Why2, Review


class WhyAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic','text')


class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic')


class Why2Admin(admin.ModelAdmin):
    list_display = ('text',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'pic', 'text')


admin.site.register(Why, WhyAdmin)
admin.site.register(Why2, Why2Admin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Review, ReviewAdmin)
