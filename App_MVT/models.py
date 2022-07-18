from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_nac = models.DateField()  
    edad = models.IntegerField()

class Miembro(models.Model):
    nombre= models.CharField(max_length=50)

class Persona(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_nac= models.CharField(max_length=50)
    edad = models.IntegerField()

    
        
