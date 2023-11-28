from rest_framework import serializers
from core.models.detalleFactura import DetalleFactura

class DetalleFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        models = DetalleFactura
        fields = ['idConsecutivo','camisetaColor','valorCamiseta''valorEstampar']
        