from django.contrib import admin
from .models import User,Company,CompanyApprentice,Products
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=['username','fullname','phone_number',]
    

admin.site.register(User,UserAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner','location']
admin.site.register(Company,CompanyAdmin)
admin.site.register(CompanyApprentice)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','type','product']

admin.site.register(Products,ProductAdmin)