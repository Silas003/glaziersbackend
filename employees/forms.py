from django import forms
from .models import Apprentice,ApprenticeLife,ApprenticeRoot

class ApprenticeForm(forms.ModelForm):
    
    class Meta:
        model=Apprentice
        fields='__all__'


class ApprenticeRootForm(forms.ModelForm):
    
    class Meta:
        model=ApprenticeRoot
        fields='__all__'

class ApprenticeLifeForm(forms.ModelForm):
    
    class Meta:
        model=ApprenticeLife
        fields='__all__'

# class ApprenticeCompanyForm(forms.ModelForm):
    
#     class Meta:
#         model=ApprenticeCompany
#         fields='__all__'