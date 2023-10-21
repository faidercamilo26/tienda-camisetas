from django.db import models

class TipoPersona(models.Model):
    idTipoPersona = models.IntegerField(primary_key=True)
    nombreTipoPersona = models.CharField(max_length=20)
    

    def __str__(self):
        return self.nombreTipoPersona