from django.db import models

class Room(models.Model):
  number = models.IntegerField()
  maxPeople = models.IntegerField()
  type_choices = (
    ('S', 'single'),
    ('D', 'double'),
    ('B', 'bimonee'),
  )
  type = models.CharField(max_length=255, 
                          choices=type_choices) 
  price = models.DecimalField(max_digits=8, 
                              decimal_places=2)

class Slot(models.Model):
  room = models.ForeignKey(Room)
  serie = models.IntegerField()
