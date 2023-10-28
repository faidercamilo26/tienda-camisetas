from rest_framework import serializers
from core.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ['username', 'nombre', 'apellido', 'tipo_documento', 'tipo_persona', 'numero_documento','correo', 'numeroCelular', 'direccion',]