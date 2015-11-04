# coding=utf-8
from django.views.generic import ListView, DetailView

__author__ = 'alexy'


class ExtraContext(object):
    extra_context = {}

    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class ExtraListView(ExtraContext, ListView):
    pass


class ExtraDetailView(ExtraContext, DetailView):
    pass
