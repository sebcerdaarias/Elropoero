from django import forms

from .models import Productos, Userreset


class ProductForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('nombre', 'imagen', 'valor', 'descripcion', 'active',)


class UserresetForm(forms.ModelForm):

    class Meta:
        model = Userreset
        fields = ['nombreusuario', ]
