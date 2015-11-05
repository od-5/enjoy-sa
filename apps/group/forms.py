# coding=utf-8
from django.forms import ModelForm, HiddenInput, TextInput, Textarea
from .models import GroupComment

__author__ = 'alexy'


class GroupCommentForm(ModelForm):
    class Meta:
        model = GroupComment
        exclude = []
        widgets = {
            'user': HiddenInput(),
            'group': HiddenInput(),
            'text': Textarea(attrs={'class': 'form-control'}),
        }
