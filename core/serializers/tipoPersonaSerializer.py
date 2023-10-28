from rest_framework import serializers
from core.models.tipoPersona import TipoPersona

class TipoPersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPersona
        fields = ['idTipoPersona', 'nombreTipoPersona']