from django.db import models 
from .detalleFactura import DetalleFactura
from .persona import Persona

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    detalleFactura = models.ForeignKey(DetalleFactura, on_delete=models.CASCADE, related_name='factura')
    nombrePersona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='factura')