from django.db import models

# Create your models here.

class publicacion(models.Model):
    nombre_apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    dificultad = models.CharField(max_length=50)
    comentario = models.TextField()
    imagen = models.ImageField(upload_to='imagenes_publicacion')

    def __str__(self):
        return "Nombre: "+ self.nombre_apellido +"," + " Título: " + self.titulo + ", Autor: " + self.autor