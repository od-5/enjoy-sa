from django.forms import ModelForm, HiddenInput, TextInput
from .models import Travel

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
