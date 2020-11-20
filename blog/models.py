from django.db import models
from django.utils import timezone


class imagenes(models.Model):
    name = models.CharField(max_length=200)
    imagen = models.TextField()
    active = models.BooleanField(default=False)

    def activate(self):
        self.active = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()


class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField()
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def activate(self):
        self.active = True
        self.save()

    def deactivate(self):
        self.active = False
        self.save()


class Userreset(models.Model):
    nombreusuario = models.CharField(max_length=50)
