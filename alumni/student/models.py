from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class studinfo1(models.Model):
   name=models.CharField(max_length=30, null=True)
   lastname=models.CharField(max_length=30, null=True)
   idnumber=models.IntegerField(primary_key=True)
   jobstatus=models.CharField(max_length=30, null=True)
   passout=models.IntegerField(default=2000)
   branch= models.CharField(max_length=30, null=True)
   email=models.EmailField(null=True)
   mobile=models.SmallIntegerField(null=True)

