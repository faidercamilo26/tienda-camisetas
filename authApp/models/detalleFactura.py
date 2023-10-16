from django.db import models 
from .camisetaColor import CamisetaColor
from .estampado import Estampado

class DetalleFactura(models.Model):
    idConsecutivo = models.AutoField(primary_key=True)
    camisetaColor = models.ForeignKey(CamisetaColor, on_delete= models.CASCADE, related_name='detalle_factura')
    estampado = models.ForeignKey(Estampado, on_delete= models.CASCADE, related_name='detalle_factura')
    valorCamiseta = models.FloatField()
    valorEstampado = models.FloatField()
    valorEstampar = models.FloatField(default=20000.0)
    