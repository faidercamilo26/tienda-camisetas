from  rest_framework import serializers
from core.models.color import Color  

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        models = Color  
        fields = ['colorId', 'nombreColor']