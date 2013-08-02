# -*- coding: utf-8 -*-

from django.db import models

class Serie(models.Model):
  serie_choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
  )
  serie = models.IntegerField(
    choices=serie_choices,
    unique=True
  ) 
 
  def __unicode__(self):
    return u"Série " + unicode(self.serie)

class Room(models.Model):
  number = models.IntegerField(unique=True)
  number.short_description = u'Numéro'
  maxPeople = models.IntegerField()
  series = models.ManyToManyField(Serie, through="Slot")
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
    return unicode(self.pk)

  def trad_number(self):
    return self.number

  def trad_maxPeople(self):
    return self.maxPeople
  
  def series_list(self):
    return ', '.join([unicode(s.serie) for s in self.series.all()])
                
  series_list.short_description = u'séries'
  trad_number.short_description = u'numéro'
  trad_maxPeople.short_description = u'maximum occupants'

class Slot(models.Model):
  room = models.ForeignKey(Room)
  serie = models.ForeignKey(Serie)

  def __unicode__(self):
    return str(self.room.number) + " - " + unicode(self.serie)


