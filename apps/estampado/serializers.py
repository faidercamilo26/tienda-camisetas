from rest_framework import serializers
from .models import Estampado

class EstampadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estampado
        fields = ['id', 'artista', 'nombre', 'foto', 'descripcion', 'precio', 'category', 'cantidad', 'ventas', 'fecha_creacion']
