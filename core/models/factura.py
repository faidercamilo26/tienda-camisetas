from django.db import models 
from .detalleFactura import DetalleFactura
from .user import User

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    detalleFactura = models.ForeignKey(DetalleFactura, on_delete=models.CASCADE, related_name='factura')
    nombrePersona = models.ForeignKey(User, on_delete=models.CASCADE, related_name='factura')