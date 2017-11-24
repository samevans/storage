from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
)

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wizrobe.views.home', name='home'),
    url(r'^contact-us/$', 'wizrobe.views.contactus', name='contactus'),
    
    # Sign In
    url(r'^sign-up/$', 'wizrobe.views.signup', name='signup'),
    url(r'^login/$', login, {'template_name': 'signin.html'}, name='signin'),
    url(r'^logout/$', 'wizrobe.views.signout', name='signout'),
    url(r'^requestpassword/$', password_reset, name='requestpassword'),
    url(r'^requestpassword/done/$', password_reset_done, name='password_reset_done'),
    url(r'^requestpassword/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^requestpassword/complete/$', password_reset_complete, name='password_reset_complete'),

    # Profiles
    url(r'^profile/$', 'wizrobe.views.view_profile', name='viewprofile'),
    url(r'^settings/profile/', 'wizrobe.views.settings_profile', name='settingsprofile'),
    url(r'^settings/account/', 'wizrobe.views.settings_account', name='settingsaccount'),
    url(r'^accounts/profile/$', 'wizrobe.views.successfully_loggedin', name='accounts_profile'),
    
    url(r'^dashboard/$', 'wizrobe.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)