# coding=utf-8
from django.contrib import admin
from .models import Why, Document, Photo, Why2, Review, Header


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


class HeaderAdmin(admin.ModelAdmin):
    list_display = ('text', 'block')


admin.site.register(Why, WhyAdmin)
admin.site.register(Why2, Why2Admin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Header, HeaderAdmin)
