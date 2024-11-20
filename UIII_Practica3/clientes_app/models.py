from django.db import models
# Create your models here.

class Cliente(models.Model):
    codigo=models.CharField(primary_key=True,max_length=60)
    nombre=models.CharField(max_length=100)
    numero=models.PositiveSmallIntegerField()
    direccion=models.CharField(max_length=60)
    interes=models.PositiveSmallIntegerField()
    historial=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    def __str__(self):
        return self.nombre
