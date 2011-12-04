from django.conf.urls.defaults import patterns, include, url

# Enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'call_center.views.home', name='home'),
    # url(r'^call_center/', include('call_center.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
