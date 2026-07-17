from django.db import models

# Create your models here.

class Estudiante(models.Model):
    cedula = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    titulo = models.FileField(upload_to='titulo/', null=True, blank=True)
    notas = models.FileField(upload_to='notas/', null=True, blank=True)
    cedula_foto = models.FileField(upload_to='cedula/', null=True, blank=True)