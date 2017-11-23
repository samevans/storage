from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'wizrobe.views.home', name='home'),
    url(r'^contact-us/$', 'wizrobe.views.contactus', name='contactus'),
    
    # Sign In
    url(r'^sign-up/$', 'wizrobe.views.signup', name='signup'),
    url(r'^login/$', login, {'template_name': 'signin.html'}, name='signin'),
    url(r'^logout/$', 'wizrobe.views.signout', name='signout'),
    url(r'^requestpassword/$', 'wizrobe.views.requestpassword', name='requestpassword'),
    
    # Profile
    url(r'^profile/$', 'wizrobe.views.view_profile', name='viewprofile'),
    url(r'^profile/edit/', 'wizrobe.views.edit_profile', name='editprofile'),
    url(r'^accounts/profile/$', 'wizrobe.views.successfully_loggedin', name='accounts_profile'),
    
    url(r'^dashboard/$', 'wizrobe.views.dashboard', name='dashboard'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)