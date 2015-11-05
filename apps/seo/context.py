import datetime
from .models import Page

__author__ = 'alexy'


def seo_setup(request):
    page = '/' + request.path.split('/')[1] + '/'
    page_slug = request.path.split('/')[1]
    if page_slug == '':
        page_slug = 'home'
    try:
        qs = Page.objects.get(page=page_slug)
    except:
        qs = False
    return {
        'page': qs,
    }
