from rest_framework import serializers
from authApp.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nombre','apellido','numero_documento' , 'username', 'password']
        
def create(self, validated_data):
    accountData = validated_data.pop()