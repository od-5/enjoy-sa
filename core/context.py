import datetime
from .models import Setup, Contacts

__author__ = 'alexy'


def site_setup(request):
    try:
        qss = Setup.objects.all().first()
    except:
        qss = None
    try:
        qsc = Contacts.objects.all().first()
    except:
        qsc = None
    if request.path == '/':
        home = True
    else:
        home = False
    print request.path.split('/')
    return {
        'SETUP': qss,
        'CONTACT': qsc,
        'CURRENT_YEAR': datetime.datetime.now(),
        'HOME_PAGE': home,
    }
