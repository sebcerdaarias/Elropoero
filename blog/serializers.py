from rest_framework import serializers
from .models import Productos, imagenes


class ProductosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['nombre', 'imagen', 'valor', 'descripcion']


class imagenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = imagenes
        fields = ['name', 'imagen']
