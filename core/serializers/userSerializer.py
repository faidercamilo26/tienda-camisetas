from rest_framework import serializers
from core.models.user import User
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id',
            'username', 'nombre', 'apellido', 'tipo_documento', 'numero_documento', 'tipo_persona', 
            'email', 'numeroCelular', 'direccion',)
