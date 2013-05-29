# Create your views here.

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from userprofile.models import UserProfile

@login_required
def display(request):
  
  try:
    userprofile = UserProfile.objects.get(pk=request.user)
  except UserProfile.DoesNotExist:
    return render(request, "userprofile/userprofile_display_trunc.html")
  
  return render(request, "userprofile/userprofile_display_full.html", {'username': request.user.username})
