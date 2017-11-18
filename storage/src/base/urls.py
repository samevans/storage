from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wizrobe.views.home', name='home'),
    url(r'^contact-us/$', 'wizrobe.views.contactus', name='contactus'),
    url(r'^sign-up/$', 'wizrobe.views.signup', name='signup'),
    url(r'^sign-in/$', 'wizrobe.views.signin', name='signin'),
    url(r'^request-password/$', 'wizrobe.views.requestpassword', name='requestpassword'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)