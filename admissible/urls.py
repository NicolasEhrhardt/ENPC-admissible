from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # static pages
    ('^page/', include('django.contrib.flatpages.urls')),
    
    # registration
    (r'^accounts/', include('registration.urls')),
    
    # profile
    url(r'^profile/', include('userprofile.urls')),
    
    # booking
    url(r'^booking/', include('booking.urls')),


    # fiber
    (r'^api/v2/', include('fiber.rest_api.urls')),
    (r'^admin/fiber/', include('fiber.admin_urls')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', {'packages': ('fiber',),}),
    
    # paypal
    (r'^cddc97f40a80aae9ad389d9d0c8f8a4e/', include('paypal.standard.ipn.urls')),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # media
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    # fiber last
    (r'', 'fiber.views.page'), # this should always be placed last
)
