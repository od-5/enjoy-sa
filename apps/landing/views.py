# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render
from .models import Why, Document, Photo, Why2, Review, Header


__author__ = 'alexy'


def home_view(request):
    why_list = Why.objects.all()
    why2_list = Why2.objects.all()
    doc_list = Document.objects.all()
    photo_list = Photo.objects.all()
    review_list = Review.objects.all()
    context = {
        'why_list': why_list,
        'why2_list': why2_list,
        'document_list': doc_list,
        'photo_list': photo_list,
        'review_list': review_list
    }
    header_list = Header.objects.all()
    for i in range(1, 10):
        var_name = 'header_%s' % i
        try:
            var_value = header_list.get(block=i)
        except:
            var_value = False
        context.update({var_name: var_value})

    return render(request, 'landing.html', context)
