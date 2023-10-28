from rest_framework import generics
from core.models.tipoPersona import TipoPersona
from core.serializers.tipoPersonaSerializer import TipoPersonaSerializer

class TipoListCreateView(generics.ListCreateAPIView):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoPersonaSerializer
