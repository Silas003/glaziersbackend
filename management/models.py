from django.db import models
from django.contrib.auth.models import AbstractUser
from employees.models import Apprentice

class User(AbstractUser):
    fullname = models.CharField(max_length=100)
    username=models.CharField(max_length=100,unique=True)
    phone_number = models.CharField(unique=True,max_length=10)
    password = models.CharField(max_length=100)
   
    def  __str__(self):
       return self.username


class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey('management.User',on_delete=models.CASCADE,related_name='company')
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class CompanyApprentice(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name='company')
    apprentice = models.ForeignKey(Apprentice,on_delete=models.CASCADE,related_name='apprentice') 

































# class Master(models.Model):
#     name=models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='management')
#     DOB=models.DateField()
#     age=models.IntegerField()
#     sex=models.CharField(max_length=25)
#     phone=models.CharField(max_length=10,unique=True)
    
#     def __str__(self):
#         return self.name

# class MasterRoot(models.Model):
#     master=models.ForeignKey(Master,on_delete=models.CASCADE,related_name='masterroot')
#     father=models.CharField(max_length=100)
#     mother=models.CharField(max_length=100)
#     nationality=models.CharField(max_length=100)

# class MasterLife(models.Model):
#     master=models.ForeignKey(Master,on_delete=models.CASCADE,related_name='masterlife')
#     region=models.CharField(max_length=100)
#     religion=models.CharField(max_length=100)
#     town=models.CharField(max_length=100)
#     house_no=models.CharField(max_length=100)
#     marital_status=models.CharField(max_length=100)
#     education=models.CharField(max_length=100)