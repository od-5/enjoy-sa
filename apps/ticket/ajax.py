# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from .forms import TicketForm

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def ticket(request):
    # try:
    #     email = Setup.objects.all()[0].email
    # except:
    #     email = 'od-5@yandex.ru'
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.ticket_status = 1
            ticket.save()
            if ticket.comment:
                message = u'Имя: %s\nE-mail: %s\nСообщение: %s\n' % (ticket.name, ticket.email, ticket.comment)
            else:
                message = u'Имя: %s\nE-mail: %s\n' % (ticket.name, ticket.email)
            send_mail(
                u'enjoy-africa.ru - Заявка с сайта',
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['od-5@yandex.ru', ]
            )
            return {
                'success': 'Message send'
            }

    return {
        'success': True
    }
