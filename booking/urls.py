from django.conf.urls.defaults import *
from booking.views import status, addQueue

urlpatterns = patterns ('',
                        url(r'^status$', 
                          status,
                          name='booking_status'),
                        url(r'^add$', 
                          addQueue,
                          name='booking_add'),
              )
