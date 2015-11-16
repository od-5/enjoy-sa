# coding=utf-8
from annoying.decorators import ajax_request
from django.db.models import Max, Min
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView
from .forms import GroupCommentForm
from .models import Group, GroupSection

__author__ = 'alexy'


class GroupListView(ListView):
    model = Group

    def get_queryset(self):
        qs = Group.objects.all()
        if self.request.GET.get('section'):
            es_pk = int(self.request.GET.get('section'))
            queryset = qs.filter(groupsection__pk=es_pk)
        elif self.request.GET.get('min') and self.request.GET.get('max'):
            min_price = int(self.request.GET.get('min'))
            max_price = int(self.request.GET.get('max'))
            queryset = qs.filter(price__gte=min_price).filter(price__lte=max_price)
        else:
            queryset = qs
            # print(qs.aggregate(Max('price')))
        return queryset

    def get_context_data(self, **kwargs):
        context = super(GroupListView, self).get_context_data(**kwargs)
        qs = Group.objects.all()
        context.update(
            qs.aggregate(Min('price'))
        )
        context.update(
            qs.aggregate(Max('price'))
        )
        print qs.aggregate(Max('price'))
        print qs.aggregate(Min('price'))
        context.update({
            'group_section_list': GroupSection.objects.all()
        })
        return context


class GroupDetailView(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        context = super(GroupDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            comment_form = GroupCommentForm(
                initial={
                    'group': self.object,
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
        form = GroupCommentForm(request.POST)
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
        return HttpResponseRedirect('/groups/')