# coding=utf-8
from django.views.generic import ListView
from .models import Excurse, ExcurseSection

__author__ = 'alexy'


class ExcurseListView(ListView):
    model = Excurse

    def get_queryset(self):
        qs = Excurse.objects.all()
        if self.request.GET.get('section'):
            es_pk = int(self.request.GET.get('section'))
            queryset = qs.filter(section__pk=es_pk)
        else:
            queryset = qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ExcurseListView, self).get_context_data(**kwargs)
        context.update({
            'excurse_section_list': ExcurseSection.objects.all()
        })
        return context