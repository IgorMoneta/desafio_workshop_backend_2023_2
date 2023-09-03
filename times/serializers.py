from rest_framework import serializers
from .models import * 

class TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ['id','time'] 

class CaracteriticasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Caracteristicas
        fields = ['id', 'estadio', 'cidade', 'time']
        