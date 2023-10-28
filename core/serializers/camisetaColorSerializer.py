from rest_framework import serializers
from core.models.camisetaColor import CamisetaColor

class CamisetaColorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = CamisetaColor
        fields = ['idCamisetaColor', 'idCamiseta', 'idColor',]