
from django.db import models
class Nombre(models.Model):
    nombre = models.CharField(max_length=100)   
    def __str__(self):
       return self.nombre
# Create your models here.
