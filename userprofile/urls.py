from django.conf.urls.defaults import *
from userprofile import views

urlpatterns = patterns ('',
                        url(r'', 
                        views.display,
                        name='raw_display'),
                      )
