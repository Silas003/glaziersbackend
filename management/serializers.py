from rest_framework import serializers
from .models import User,Company,CompanyApprentice
from employees.serializers import ApprenticeSerializer

class UserRegSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['fullname', 'phone_number', 'username', 'password']
        

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['fullname', 'phone_number', 'username','id']
        
class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']


class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'


class CompanyApprenticeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyApprentice
        fields=['apprentice','company' ]
        

class CompanySerializers(serializers.ModelSerializer):
    company=CompanyApprenticeSerializer(many=True,read_only=True)
    class Meta:
        model=Company
        fields=['id','owner','name','location','company',]
        # depth=1