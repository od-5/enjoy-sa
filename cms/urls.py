from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import debug_toolbar
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='home'),
    url(r'^travels/', include('apps.travel.urls', namespace='travels'),),
    url(r'^groups/', include('apps.group.urls', namespace='groups'),),
    url(r'^excurse/', include('apps.excurse.urls', namespace='excurse'),),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += patterns(
        '',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
