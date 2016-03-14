from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserTotal(models.Model):
    account_id = models.TextField()
    value = models.IntegerField()
    created_at = models.DateTimeField()

class Passbook(models.Model):
    value = models.IntegerField()
    created_at = models.DateTimeField()
    