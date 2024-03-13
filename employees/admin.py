from django.contrib import admin
from .models import Apprentice,ApprenticeLife,ApprenticeRoot
# Register your models here.

class ApprenticeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'phone_number','DOB','sex']
    

admin.site.register(Apprentice,ApprenticeAdmin)

class ApprenticeLifeAdmin(admin.ModelAdmin):
    list_display = ['apprentice','region','religion','marital_status']
    

admin.site.register(ApprenticeLife,ApprenticeLifeAdmin)

class ApprenticeRootAdmin(admin.ModelAdmin):
    list_display =['apprentice','father','mother','nationality','hometown',]
    

admin.site.register(ApprenticeRoot,ApprenticeRootAdmin)