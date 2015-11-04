# coding=utf-8
from annoying.decorators import ajax_request
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import UpdateView
from core.forms import UserProfileForm
from core.models import Setup, User

__author__ = 'alexy'


def get_robots_txt(request):
    try:
        content = Setup.objects.all()[0].robots_txt
    except:
        content = u'User-agent: *'
    robots_response = HttpResponse(content, content_type='text/plain')
    return robots_response


@ajax_request
def landing_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    error = u'Вы ввели неверный e-mail или пароль'
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
        else:
            return {
                'error': error
            }
    else:
        return {
            'error': error
        }

@ajax_request
def landing_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            exist_user = User.objects.get(email=username)
        except:
            exist_user = None
        if exist_user:
            return {
                'error': u'Пользователь с таким email уже зарегистрирован в системе!'
            }
        else:
            user = User.objects.create_user(username, password)
            user.is_staff = True
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request, user)
            return {
                'success': u'Вы успешно зарегистрировались на сайте!'
            }


class UserUpdateView(UpdateView):
    model = User
    template_name = 'core/profile.html'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user
