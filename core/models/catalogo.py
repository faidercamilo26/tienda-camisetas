from django.db import models 
from .camisetaColor import CamisetaColor
from .estampado import Estampado

class Catalogo(models.Model):
    idCatalogo = models.IntegerField(primary_key=True)
    camisetaColor = models.ForeignKey(CamisetaColor, on_delete= models.CASCADE, related_name='catalogo')
    estampado = models.ForeignKey(Estampado, on_delete= models.CASCADE, related_name='catalogo')
    