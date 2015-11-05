# coding=utf-8
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView
from core.models import User
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


class TravelListView(ListView):
    model = Travel

    def get_queryset(self):
        qs = Travel.objects.all()
        if self.request.GET.get('author'):
            author_pk = int(self.request.GET.get('author'))
            queryset = qs.filter(user__pk=author_pk)
        else:
            queryset = qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super(TravelListView, self).get_context_data(**kwargs)
        context.update({
            'author_list': User.objects.filter(first_name__isnull=False, last_name__isnull=False).exclude(avatar='')
        })
        return context