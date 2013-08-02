from django.contrib import admin
from room.models import Room, Slot, Serie

class SlotInline(admin.TabularInline):
  model = Slot
  extra = 1

class RoomAdmin(admin.ModelAdmin):
  list_display = ('trad_number', 'trad_maxPeople', 'series_list')
  inlines = (SlotInline,)

admin.site.register(Room, RoomAdmin)

class SerieAdmin(admin.ModelAdmin):
  pass

admin.site.register(Serie, SerieAdmin)
