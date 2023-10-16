from django.db import models 

class Camiseta(models.Model):
    idCamiseta = models.IntegerField(primary_key=True)
    talla = models.CharField(max_length=3)
    