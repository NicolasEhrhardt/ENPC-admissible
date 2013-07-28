from django.db import models

from django.contrib.auth.models import User
from room.models import Slot

from datetime import datetime, timedelta
from django.utils.timezone import utc

from django.conf import settings

class SlotBooked(models.Model):
  user = models.ForeignKey(User, unique=True)
  slot = models.ForeignKey(Slot, unique=True)
  dateBooked = models.DateTimeField('Date Booked')
  datePaid = models.DateTimeField('Date Paid', null=True)
  
  def isPaid(self):
    if datePaid == Field.null:
      return False
    else:
      return True

  def dateLimit(self):
    return self.dateBooked + timedelta(days=settings.DAYS_TO_PAY)

  def isExpired(self):
    return dateLimit() > datetime.utcnow().replace(tzinfo=utc)

class Queue(models.Model):
  user = models.ForeignKey(User, unique=True)
  serie = models.IntegerField()
  maxPeople_preference = models.IntegerField()
  dateAdded = models.DateTimeField('Date Added')
