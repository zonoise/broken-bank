from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserTotal(models.Model):
    created_at = models.DateTimeField()

class Passbook(models.Model):
    created_at = models.DateTimeField()
    