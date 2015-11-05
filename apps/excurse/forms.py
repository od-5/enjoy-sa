# coding=utf-8
from django.forms import ModelForm, HiddenInput, TextInput, Textarea
from .models import ExcurseComment

__author__ = 'alexy'

class ExcurseCommentForm(ModelForm):
    class Meta:
        model = ExcurseComment
        exclude = []
        widgets = {
            'user': HiddenInput(),
            'excurse': HiddenInput(),
            'text': Textarea(attrs={'class': 'form-control'}),
        }
