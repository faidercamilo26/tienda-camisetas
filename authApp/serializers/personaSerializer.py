from rest_framework import serializers
from authApp.models.persona import Persona

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ['nombre','apellido','numero_documento' , 'username', 'password']
        
def create(self, validated_data):
    accountData = validated_data.pop()