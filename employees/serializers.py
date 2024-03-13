from rest_framework import serializers
from .models import Apprentice,ApprenticeLife,ApprenticeRoot
from cloudinary.forms import CloudinaryFileField

class ApprenticeSerializer(serializers.ModelSerializer):
    # image=CloudinaryFileField(
    #      options={"folder": "apprentice/", "crop": "limit", "width": 600, "height": 600,}
    # )
    image = serializers.ImageField(use_url=True, required=False, allow_null=True)
    class Meta:
        model=Apprentice
        fields=['id','fullname','phone_number','sex','DOB','image']

        depth=1
        
class ApprenticeRootSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApprenticeRoot
        fields='__all__'
        # depth=1



class ApprenticeLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApprenticeLife
        fields='__all__'
        # depth=1