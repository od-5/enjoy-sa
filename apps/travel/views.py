# coding=utf-8
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from .models import Travel
from .forms import TravelCreateForm

__author__ = 'alexy'


class TravelCreateView(CreateView):
    model = Travel
    form_class = TravelCreateForm

    def get_initial(self):
        username = self.request.user
        return {
            'user': username,
        }
