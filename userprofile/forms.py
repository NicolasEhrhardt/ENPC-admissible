# -*- coding: utf-8 -*-

from django import forms

class UserProfileForm(forms.Form):
  firstname = forms.CharField(
    label=u'Prénom', 
    max_length=255)
  lastname = forms.CharField(
    label=u'Nom', 
    max_length=255)
  number = forms.CharField(
    label=u'Numéro de candidat', 
    max_length=255)
  serie_choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
  )
  serie = forms.ChoiceField(
    label=u'Série',
    choices=serie_choices)
  sexe_choices = (
    ('M', 'Homme'),
    ('F', 'Femme'),
  )
  sexe = forms.ChoiceField(
    label=u'Sexe',
    choices=sexe_choices) 
  phoneNumber = forms.CharField(
    label=u'Téléphone',
    max_length=255)
