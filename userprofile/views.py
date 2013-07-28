# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from userprofile.models import UserProfile
from userprofile.forms import UserProfileForm

@login_required
def display(request):
  
  try:
    userprofile = UserProfile.objects.get(pk=request.user)
  except UserProfile.DoesNotExist:
    return render(request, "userprofile/userprofile_display_trunc.html")
  
  return render(request, "userprofile/userprofile_display_full.html", 
    {
      'username': request.user.username,
      'firstname': userprofile.firstname,
      'lastname': userprofile.lastname,
      'number': userprofile.number,
      'serie': userprofile.serie,
      'sexe': userprofile.sexe,
      'phoneNumber': userprofile.phoneNumber,
    })

@login_required
def edit(request):
  if request.method == 'POST': # If the form has been submitted...
    form = UserProfileForm(request.POST) # A form bound to the POST data
  
    if form.is_valid(): 
      userprofile = UserProfile()
      userprofile.user = request.user
      userprofile.firstname = form.cleaned_data['firstname']
      userprofile.lastname = form.cleaned_data['lastname']
      userprofile.number = form.cleaned_data['number']
      userprofile.serie = form.cleaned_data['serie']
      userprofile.sexe = form.cleaned_data['sexe']
      userprofile.phoneNumber = form.cleaned_data['phoneNumber']

      userprofile.save()
      return redirect('userprofile.views.display') # Redirect after POST
    else:
      return render(request,
        'userprofile/userprofile_edit.html', {
            'form': form,
          }
        )
  else:
    try:
      userprofile = UserProfile.objects.get(pk=request.user)
      form = UserProfileForm({
        'firstname': userprofile.firstname,
        'lastname': userprofile.lastname,
        'number': userprofile.number,
        'serie': userprofile.serie,
        'sexe': userprofile.sexe,
        'phoneNumber': userprofile.phoneNumber,
      })
    except Exception as ex:
      print ex
      form = UserProfileForm()

    return render(request, 
            'userprofile/userprofile_edit.html', {
                'form': form,
              }
            )
