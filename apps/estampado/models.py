from django.db import models 
from datetime import datetime
from core.models.user import User
from apps.category.models import Category 

from django.conf import settings
domain = settings.DOMAIN

class Estampado(models.Model):
    artista = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre =  models.CharField(max_length=30)
    foto = models.ImageField(upload_to='photos/%Y/%m')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    ventas = models.IntegerField(default=0) 
    fecha_creacion = models.DateTimeField(default=datetime.now)
    
    def get_thumbnail(self):
        if self.foto:
            return self.foto.url
        return ''
    
    def __str__(self):
        return self.nombre
