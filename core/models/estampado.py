from django.db import models 

class Estampado(models.Model):
    idEstampado = models.IntegerField(primary_key=True)
    nombre =  models.CharField(max_length=30)
    descripcion = models.TextField()
    estampas = models.BinaryField()