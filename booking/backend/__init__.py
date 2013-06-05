from booking.models import Queue, SlotBooked
from room.models import Slot
from datetime import datetime
from django.utils.timezone import utc
from django.db import transaction

def addQueue(user, serie, preference):
  """
    Add a new user in the queue
  """
  entry = Queue(
            user=user, 
            serie=serie, 
            maxPeople_preference=preference,
            date=datetime.utcnow().replace(tzinfo=utc)
          )
  entry.save()

@transaction.commit_on_success
def refreshBooking(serie):
  """
    refresh booking for a particular serie
  """
  # get room available for this serie that are not booked
  slotEmpty = list(Slot.objects
                   .filter(
                     serie=serie, 
                     slotbooked__isnull=True
                   )
                   .order_by('room__maxPeople'))
  # get people awaiting in the queue sorted by date of arrival
  queueAwaiting = list(Queue.objects
                       .filter(
                        serie=serie
                       )
                       .order_by('date'))

  # assigning room for people in the queue until there is no space
  while len(slotEmpty) > 0 and len(queueAwaiting) > 0:
    processingQueue = queueAwaiting.pop(0)
   
    # taking the room that matches the user preference (default is max of maxPeople)
    if processingQueue.maxPeople_preference == 1:
      processingSlot = slotEmpty.pop(0)
    else:
      processingSlot = slotEmpty.pop(-1)
    
    assignSlot(processingQueue.user, processingSlot)
    processingQueue.delete()

def assignSlot(user, slot):
  booking = SlotBooked(
              user=user, 
              slot=slot, 
              dateBooked=datetime.utcnow().replace(tzinfo=utc),
              datePaid=None
            )
  booking.save()

  # should send an email here
