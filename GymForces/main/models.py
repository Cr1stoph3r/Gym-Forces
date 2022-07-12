from django.db import models

# Create your models here.

class Registro(models.Model):
    user = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return self.user

opciones_deporte = [
    [0, 'Deporte'],
    [1, 'Gym'],
    [2, 'Krav-maga'],
    [3, 'yoga']
]
class galeria(models.Model):
    deporte = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="registro", null=True)
    def __str__(self):
        return self.deporte

class contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    deporte_consulta = models.IntegerField(choices=opciones_deporte)
    mensaje = models.TextField()
    avisos = models.BooleanField()
    def __str__(self):
        return self.nombre