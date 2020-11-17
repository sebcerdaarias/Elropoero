from django import forms

from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


# class ImgFrom(forms.ModelForm)
#
#    class Meta:
#        model = imagen
#        fields = ('name', 'imagen')'''
