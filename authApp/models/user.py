from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from .tipoPersona import TipoPersona

class UserManager(BaseUserManager):
    def create_user(self, username , password=None ):
        """"
        Creates and saves a user with the given username and password.
        """
        if not username:
            raise ValueError('Los usuarios deben tener un username')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password):
        """"
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user
    
    
class User(AbstractBaseUser, models.Model):
    numero_documento = models.IntegerField( primary_key=True)
    username = models.CharField('Username',max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=64, choices = (('CC', 'Cedula de ciudadania'), ('CE','Cedula de extranjeria'),('TI', 'Tarjeta d identidad') ))
    tipo_persona = models.ForeignKey(TipoPersona, on_delete= models.CASCADE , related_name='tipoPersona')
    nombre = models.CharField('Nombre', max_length=20)
    apellido = models.CharField(max_length=20)
    correo= models.CharField('Email', max_length=30, unique = True)
    numeroCelular = models.CharField(max_length=10, unique=True, help_text="Ingrese un número de celular de 10 dígitos")
    direccion = models.CharField(max_length=50)
    isActive = models.BooleanField(default=True)

    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        

        
    objects = UserManager()
    USERNAME_FIELD = 'username'
