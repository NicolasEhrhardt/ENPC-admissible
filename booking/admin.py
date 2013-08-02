from django.contrib import admin
from booking.models import SlotBooked, Queue

class SlotBookedAdmin(admin.ModelAdmin):
  pass

admin.site.register(SlotBooked, SlotBookedAdmin)

class QueueAdmin(admin.ModelAdmin):
  pass

admin.site.register(Queue, QueueAdmin)
