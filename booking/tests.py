"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from booking import backend
from booking.models import Queue, SlotBooked
from room.models import Slot, Room
from django.contrib.auth.models import User

from time import sleep

class ModelTest(TestCase):
  def setUp(self):
    user = User.objects.create(username="DummyUser")
    user1 = User.objects.create(username="DummyUser1")
    user2 = User.objects.create(username="DummyUser2")
    user3 = User.objects.create(username="DummyUser3")
    user4 = User.objects.create(username="DummyUser4")

    backend.addQueue(user, 1, 1)
    
    sleep(1.0)
    backend.addQueue(user1, 1, 1)
    
    sleep(1.0)
    backend.addQueue(user2, 1, 2) 

    sleep(1.0)
    backend.addQueue(user3, 2, 1) 

    sleep(1.0)
    backend.addQueue(user4, 2, 1) 

    room = Room(number=121, maxPeople=1, type='S', price='10.00')
    room.save()
    availability = Slot(room=room, serie=1)
    availability.save()
 
    room1 = Room(number=122, maxPeople=2, type='D', price='10.00')
    room1.save()
    availability1 = Slot(room=room1, serie=2)
    availability1.save()

    room2 = Room(number=122, maxPeople=2, type='B', price='10.00')
    room2.save()
    availability1 = Slot(room=room2, serie=1)
    availability1.save()
    availability2 = Slot(room=room2, serie=1)
    availability2.save()
    
  def test_addQueue(self):
    """
    Tests adding to the queue 
    """
    self.assertEqual(len(Queue.objects.all()), 5)

  def test_refreshBooking1(self):
    """
    Tests the refresh of the booking
    """
    backend.refreshBooking(1)
    self.assertEqual(len(Queue.objects.all()), 2)
    self.assertEqual(len(SlotBooked.objects.all()), 3)
    self.assertEqual(SlotBooked.objects.all()[0].user.username, "DummyUser")
    self.assertEqual(len(SlotBooked.objects.filter(slot__room__maxPeople=1)), 1)
    self.assertEqual(len(SlotBooked.objects.filter(slot__room__maxPeople=2)), 2)

  def test_refreshBooking2(self):
    """
    Tests the refresh of the booking
    """
    self.assertEqual(len(SlotBooked.objects.all()), 0)
    backend.refreshBooking(2)
    self.assertEqual(len(SlotBooked.objects.filter(slot__serie=2)), 1)
    self.assertEqual(len(SlotBooked.objects.filter(slot__serie=1)), 0)
