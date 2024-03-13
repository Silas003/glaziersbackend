from rest_framework.routers import DefaultRouter
from .views import UserRegView,CompanyView,CompanyApprenticeView,UserLogin
from django.urls import path
from . import views
app_name='management'

router=DefaultRouter()
router.register('register',UserRegView,basename='register')
router.register('company',CompanyView,basename='company')
router.register('company-app',CompanyApprenticeView,basename='company-apprentice')
router.register('user-login',UserLogin,basename='userlogin')



urlpatterns=[
    path('user-log/',views.login_view,name='user-log'),

]

urlpatterns+=router.urls