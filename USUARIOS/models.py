from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    CHOICE = (
        ('Profesional', 'Profesional'),
        ('Estudiante', 'Estudiante'),
        ('Aficionado', 'Aficionado')
    )
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    imagen = models.ImageField(upload_to='imagenes_usuarios')
    nivel = models.CharField(max_length=11, choices=CHOICE, null=True, blank=True)
    
    def __str__(self):
        return "Usuario: " + self.usuario.username + ", Nivel: " + str(self.nivel)
