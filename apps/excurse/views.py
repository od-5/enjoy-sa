# coding=utf-8
from annoying.decorators import ajax_request
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from apps.excurse.forms import ExcurseCommentForm
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


class ExcurseDetailView(DetailView):
    model = Excurse

    def get_context_data(self, **kwargs):
        context = super(ExcurseDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            comment_form = ExcurseCommentForm(
                initial={
                    'excurse': self.object,
                    'user': self.request.user
                }
            )
            context.update({
                'comment_form': comment_form
            })
        return context


@ajax_request
def comment(request):
    if request.method == 'POST':
        form = ExcurseCommentForm(request.POST)
        print form
        if form.is_valid():
            new_comment = form.save()
            new_comment.save()
            return {
                'success': u'Ваш комментарий сохранён'
            }
        else:
            return {
                'success': u'Текст комментария не может быть пустым'
            }
    else:
        return HttpResponseRedirect('/excurse/')