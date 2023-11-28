from django.db import models
from .tipoPersona import TipoPersona
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
import os


class UserAccountManager(BaseUserManager):
    def create_user(self, username , password=None, **extra_fields ):
        if not username:
            raise ValueError('Los usuarios deben tener un username')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, password, **extra_fields):
        user = self.create_user(username,password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
    
    
class User(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True )
    username = models.CharField('Username',max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=64, choices = (('CC', 'Cedula de ciudadania'), ('CE','Cedula de extranjeria'),('TI', 'Tarjeta de identidad') ))
    numero_documento = models.IntegerField(null = True, blank = True)
    tipo_persona = models.ForeignKey(TipoPersona, on_delete= models.CASCADE , related_name='tipoPersona', null = True, blank = True)
    nombre = models.CharField('Nombre', max_length=20)
    apellido = models.CharField(max_length=20)
    email= models.EmailField('Email', max_length=30, unique = True)
    numeroCelular = models.CharField(max_length=10, unique=True, help_text="Ingrese un número de celular de 10 dígitos")
    direccion = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','tipo_documento', 'numero_documento','tipo_persona','nombre','apellido','numeroCelular','direccion',]
    
    
    def __str__(self):
        return self.nombre + " " + self.apellido

        

        
    
