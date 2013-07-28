from django.conf.urls.defaults import *
from userprofile.views import display, edit

urlpatterns = patterns ('',
                        url(r'^home$', 
                          display,
                          name='profile_home'),
                        url(r'^edit$',
                          edit,
                          name='profile_edit'),
                      )
