from django.db import models

# Create your models here.
class Challenge(models.Model):
    first_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=128)