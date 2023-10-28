from rest_framework import serializers
from core.models.catalogo import Catalogo

class CatalogoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Catalogo
        fields = ['idCatalogo', 'camisetaColor', 'estampado']