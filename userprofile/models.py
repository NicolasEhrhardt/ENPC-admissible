from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
  # Contact attributes
  user = models.OneToOneField(User, primary_key=True)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  number = models.CharField(max_length=255)
  phoneNumber = models.CharField(max_length=255)
