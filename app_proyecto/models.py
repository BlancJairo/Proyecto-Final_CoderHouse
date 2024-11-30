from django.db import models
from django.contrib.auth.models import User

class Vehiculos(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True  

    def str(self):
        return f"{self.marca}, {self.modelo}, {self.ano}"

class autos(Vehiculos):
    pass 

class Camionetas(Vehiculos):
    pass  

class Camiones(Vehiculos):
    pass  