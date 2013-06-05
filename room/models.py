# -*- coding: utf-8 -*-

from django.db import models

class Room(models.Model):
  number = models.IntegerField()
  number.short_description = u'Numéro'
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
  def trad_number(self):
    return self.number

  def trad_maxPeople(self):
    return self.maxPeople
        
  trad_number.short_description = u'numéro'
  trad_maxPeople.short_description = u'maximum occupants'

class Slot(models.Model):
  room = models.ForeignKey(Room)
  serie = models.IntegerField()
