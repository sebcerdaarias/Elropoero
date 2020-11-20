from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


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
