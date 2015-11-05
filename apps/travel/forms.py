# coding=utf-8
from django.forms import ModelForm, HiddenInput, TextInput, Textarea
from .models import Travel, TravelComment

__author__ = 'alexy'


class TravelCreateForm(ModelForm):
    class Meta:
        model = Travel
        # fields = ('user', 'travel_review', 'text')
        exclude = []
        widgets = {
            'user': HiddenInput(),
            'slug': HiddenInput(),
            'title': TextInput(attrs={'class': 'form-control'}),
            'text': TextInput(attrs={'class': 'form-control'}),
        }


class TravelCommentForm(ModelForm):
    class Meta:
        model = TravelComment
        exclude = []
        widgets = {
            'user': HiddenInput(),
            'travel': HiddenInput(),
            'text': Textarea(attrs={'class': 'form-control'}),
        }
