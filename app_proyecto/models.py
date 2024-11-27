from django.db import models
from django.contrib.auth.models import User

class autos (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100) 
    descripcion = models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.ano}"  
    
class Camionetas (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100) 
    descripcion = models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.ano}"  
    
class Camiones (models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=4)
    color = models.CharField(max_length=15)
    equipamiento = models.CharField(max_length=100) 
    descripcion = models.CharField(max_length=200)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.ano}"  
