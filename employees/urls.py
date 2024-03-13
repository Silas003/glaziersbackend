from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ApprenticeViewset,ApprenticeLifeViewset,ApprenticeRootViewset
router=DefaultRouter()

router.register('apprentice',ApprenticeViewset,basename='apprentice')
router.register('apprenticelife',ApprenticeLifeViewset,basename='apprenticeife')
router.register('apprenticeroot',ApprenticeRootViewset,basename='apprenticeroot')
# router.register('apprenticecompany',ApprenticeCompanyViewset,basename='apprenticecompany')

app_name='employees'

urlpatterns=[

]

urlpatterns+=router.urls