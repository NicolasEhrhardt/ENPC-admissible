from django.db import models

from django.contrib.auth.models import User
from room.models import Slot

class SlotBooked(models.Model):
  user = models.ForeignKey(User)
  slot = models.ForeignKey(Slot)
  date = models.DateTimeField('Date Booked')

class Queue(models.Model):
  user = models.ForeignKey(User)
  serie = models.IntegerField()
  maxPeople_preference = models.IntegerField()
  date = models.DateTimeField('Date Added')
