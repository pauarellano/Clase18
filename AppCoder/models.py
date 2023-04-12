from django.db import models
#Creamos los objetos que django va a usar para crear la DB
#Cada modelo es una tabla en la DB.
# Create your models here.
class Curso(models.Model):
    #Creamos atributos
    nombre=models.CharField(max_length=50) #Tendra máximo 50 caracteres, campo de texto
    comision=models.IntegerField() #para poner Números

    def __str__(self):
         return f"{self.nombre} - {self.comision}"

class Estudiante(models.Model):
     nombre=models.CharField(max_length=50)
     apellido=models.CharField(max_length=50)
     dni=models.IntegerField()
     email=models.EmailField()

class Profesor(models.Model):
     nombre=models.CharField(max_length=50)
     apellido=models.CharField(max_length=50)
     email=models.EmailField()
     profesion=models.CharField(max_length=50)

     def __str__(self):
          return f"{self.nombre}  {self.apellido}"

class Entregable(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_entrega=models.DateField()
    entregado=models.BooleanField()