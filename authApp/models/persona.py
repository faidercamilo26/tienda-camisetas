from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from django.db import models
from .tipoPersona import TipoPersona

class UserManager(BaseUserManager):
    def create_user(self, username , password= None):
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
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    
class Persona(AbstractBaseUser, PermissionsMixin, models.Model):
    numero_documento = models.IntegerField( primary_key=True,)
    username = models.CharField('Username',max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=4)	
    tipo_persona = models.ForeignKey(TipoPersona, on_delete= models.CASCADE , related_name='persona')
    nombre = models.CharField('Name', max_length=20)
    apellido = models.CharField(max_length=20)
    correo= models.CharField('Email', max_length=30, unique = True)
    numeroCelular = models.IntegerField(unique = True)
    dirreccion = models.CharField(max_length=50)
    password = models.CharField('Password',max_length=30)
    groups = models.ManyToManyField('auth.Group', related_name='personas')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='personas_permissions')
    
    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)
        

        
    objects = UserManager()
    USERNAME_FIELD = 'username'