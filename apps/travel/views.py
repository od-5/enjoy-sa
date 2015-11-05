# coding=utf-8
from annoying.decorators import ajax_request
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from core.models import User
from .models import Travel
from .forms import TravelCreateForm, TravelCommentForm

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


class TravelDetailView(DetailView):
    model = Travel

    def get_context_data(self, **kwargs):
        context = super(TravelDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            comment_form = TravelCommentForm(
                initial={
                    'travel': self.object,
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
        form = TravelCommentForm(request.POST)
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
        return HttpResponseRedirect('/travels/')

