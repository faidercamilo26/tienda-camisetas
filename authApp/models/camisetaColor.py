from django.db import models 
from .camiseta import Camiseta
from .color import Color

class CamisetaColor(models.Model):
    idCamisetaColor = models.AutoField(primary_key=True)
    idCamiseta = models.ForeignKey(Camiseta, on_delete = models.CASCADE, related_name='camiseta_color')
    idColor = models.ForeignKey(Color, on_delete= models.CASCADE, related_name= 'color_camiseta')
    imagenCamisetaColor = models.BinaryField()