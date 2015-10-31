# coding=utf-8
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import logout
import debug_toolbar
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', TemplateView.as_view(template_name='landing.html'), name='home'),
    url(r'^$', 'apps.landing.views.home_view', name='home'),
    url(r'^about/', include('apps.about.urls', namespace='about'),),
    url(r'^travels/', include('apps.travel.urls', namespace='travels'),),
    url(r'^groups/', include('apps.group.urls', namespace='groups'),),
    url(r'^excurse/', include('apps.excurse.urls', namespace='excurse'),),
    url(r'^ticket/', include('apps.ticket.urls', namespace='ticket'),),
    url(r'^faq/', include('apps.faq.urls', namespace='faq'),),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('core.urls')),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^inplaceeditform/', include('inplaceeditform.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
