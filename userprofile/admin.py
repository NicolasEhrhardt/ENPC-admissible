from userprofile.models import UserProfile
from django.contrib import admin

# Profile registration
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ('user', 'firstname', 'lastname')

admin.site.register(UserProfile, UserProfileAdmin)
