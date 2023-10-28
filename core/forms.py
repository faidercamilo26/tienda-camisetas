from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    Direccion = forms.CharField(max_length=255, required=True, help_text='Ingresa tu dirección de residencia.')
    ID_Usuario = forms.IntegerField(max_value=9999999999, required=True, help_text='Ingresa tu número de identificación')
    document_choices = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        
    ]
    Tipo_Documento = forms.ChoiceField(choices=document_choices, required=True, help_text='Selecciona tu tipo de documento')
    
    telefono = forms.IntegerField(max_value=9999999999, required=True, help_text='Ingresa tu número de telefono')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'Tipo_Documento', 'ID_Usuario', 'email', 'telefono', 'Direccion', 'password1', 'password2']
