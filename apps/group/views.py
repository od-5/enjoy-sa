# coding=utf-8
from annoying.decorators import ajax_request
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .forms import GroupCommentForm
from .models import Group

__author__ = 'alexy'


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