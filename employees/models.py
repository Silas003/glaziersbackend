from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Apprentice(models.Model):
    fullname=models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True)
    DOB=models.DateField(default=timezone.now)
    sex=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=10,unique=True)
    
    def __str__(self):
        return self.fullname

class ApprenticeRoot(models.Model):
    apprentice=models.ForeignKey(Apprentice,on_delete=models.CASCADE,related_name='approot')
    father=models.CharField(max_length=100)
    mother=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    hometown=models.CharField(max_length=100)
    

class ApprenticeLife(models.Model):
    apprentice=models.ForeignKey(Apprentice,on_delete=models.CASCADE,related_name='applife')
    region=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    town=models.CharField(max_length=100)
    house_no=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100)
    education=models.CharField(max_length=100)