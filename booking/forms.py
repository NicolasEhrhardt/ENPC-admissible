# -*- coding: utf-8 -*-

from django import forms

class BookingForm(forms.Form):
  maxPeople_choices = (
    (1, 1),
    (2, 2),
  )
  maxPeople_preference = forms.ChoiceField(
    label=u'Préférence du nombre d\'occupants :',
    choices=maxPeople_choices
  )
