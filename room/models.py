# -*- coding: utf-8 -*-

from django.db import models

class Room(models.Model):
  number = models.IntegerField(unique=True)
  number.short_description = u'Numéro'
  maxPeople = models.IntegerField()
  type_choices = (
    ('S', u'simple'),
    ('D', u'double'),
    ('B', u'bimonée'),
  )
  type = models.CharField(max_length=255, 
                          choices=type_choices) 
  price = models.DecimalField(max_digits=8, 
                              decimal_places=2)
  def __unicode__(self):
    return self.pk

  def trad_number(self):
    return self.number

  def trad_maxPeople(self):
    return self.maxPeople
        
  trad_number.short_description = u'numéro'
  trad_maxPeople.short_description = u'maximum occupants'

class Slot(models.Model):
  room = models.ForeignKey(Room)
  serie = models.IntegerField()

  def __unicode__(self):
    return str(self.room.number) + " - " + str(self.serie)

 
