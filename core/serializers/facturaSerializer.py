from rest_framework import serializers
from core.models.factura import Factura

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Factura
        fields = ['idFactura', 'detalleFactura', 'nombrePersona']