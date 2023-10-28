from rest_framework import serializers
from core.models.estampado import Estampado  

class EstampadoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Estampado  
        fields = ['idEstampado', 'nombre', 'descipcion', 'estampas']