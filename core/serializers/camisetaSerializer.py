from rest_framework import serializers
from core.models.camiseta import Camiseta

class CamisetaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Camiseta
        fields = ['idCamiseta', 'talla']
    