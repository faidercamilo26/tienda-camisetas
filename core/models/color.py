from django.db import models 

class Color(models.Model):
    colorId = models.IntegerField(primary_key=True)
    nombreColor = models.CharField(max_length=30)