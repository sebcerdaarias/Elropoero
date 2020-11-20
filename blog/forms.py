from django import forms

from .models import Post,Productos


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Productos
        fields = ('nombre','imagen','valor','descripcion','active',)

