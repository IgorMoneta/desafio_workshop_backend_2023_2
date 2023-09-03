from django.shortcuts import render
from rest_framework import viewsets, status
from .models import *
from .serializers import *



class TimeViewSet(viewsets.ModelViewSet):
        queryset = Time.objects.all()
        serializer_class = TimeSerializers
    
class CaracteristicaViewSet(viewsets.ModelViewSet):
        queryset = Caracteristicas.objects.all()
        serializer_class = CaracteriticasSerializers

            