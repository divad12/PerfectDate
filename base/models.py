from django.db import models
from django.contrib.auth.models import User

class freeTimes(models.Model):
  user = models.ForeignKey(User)
  startDate = models.DateTimeField()
  endDate = models.DateTimeField()

class interests(models.Model):
  user = models.ForeignKey(User)
  interest = models.CharField(max_length=255)

