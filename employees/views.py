from django.shortcuts import render,redirect
from.forms import ApprenticeRoot,ApprenticeLife,Apprentice
from .serializers import ApprenticeLifeSerializer,ApprenticeRootSerializer,ApprenticeRootSerializer,ApprenticeSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response



class ApprenticeViewset(viewsets.ModelViewSet):
    serializer_class=ApprenticeSerializer
    queryset=Apprentice.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(image=self.request.FILES.get('image'))

    def perform_update(self, serializer):
        instance = serializer.save(image=self.request.FILES.get('image'))
# class ApprenticeCompanyViewset(viewsets.ModelViewSet):
#     serializer_class=ApprenticeCompanySerializer
#     queryset=ApprenticeCompany.objects.all()

class ApprenticeLifeViewset(viewsets.ModelViewSet):
    serializer_class=ApprenticeLifeSerializer
    queryset=ApprenticeLife.objects.all()

class ApprenticeRootViewset(viewsets.ModelViewSet):
    serializer_class=ApprenticeRootSerializer
    queryset=ApprenticeRoot.objects.all()
    
    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save()