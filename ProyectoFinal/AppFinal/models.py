from django.db import models
from django.contrib.auth.models import User



class Futbol(models.Model):

    nombre_equipo = models.CharField(max_length=40)
    integrantes = models.IntegerField()
    email_representante = models.EmailField()
    telefono_contacto = models.CharField(max_length=40)
    id_torneo = models.IntegerField()
    fecha_de_registro = models.DateField()

    def __str__(self):
        return f"{self.nombre_equipo}"

class TenisSingle(models.Model):
    nombre_participante = models.CharField(max_length=40)
    email_tenista = models.EmailField()
    telefono_contacto = models.CharField(max_length=40)
    id_torneo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_participante}"

class Volley(models.Model):
    nombre_equipo = models.CharField(max_length=40)
    integrantes = models.IntegerField()
    email_representante = models.EmailField()
    telefono_contacto = models.CharField(max_length=40)
    id_torneo = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_equipo}"


class Avatar(models.Model):  

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares',null=True,blank=True)