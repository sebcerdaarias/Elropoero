from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import *
from .models import imagenes, Productos, Userreset
from django.shortcuts import render, get_object_or_404
from .forms import ProductForm, UserresetForm
from django.shortcuts import redirect
from django.utils.crypto import get_random_string

from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def index(request):
    imagene = imagenes.objects.filter(active=True)
    return render(request, 'blog/index.html', {'imagenes': imagene})


def galeria(request):
    Producto = Productos.objects.filter(active=True)
    return render(request, 'blog/galeria.html', {'Productos': Producto})


def logout(request):
    do_logout(request)
    return redirect('index')


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "blog/login.html", {'form': form})


def producto_edit(request, pk):
    if request.user.is_staff:
        producto = get_object_or_404(Productos, pk=pk)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=producto)
            if form.is_valid():
                form.save()
                return redirect('galeria')
        else:
            form = ProductForm(instance=producto)
        return render(request, 'blog/producto_edit.html', {'form': form})


def producto_del(request, pk):
    producto = Productos.objects.filter(pk=pk)
    producto.delete()
    return redirect('galeria')


def user_reset(request):
    form = UserresetForm()
    if request.method == "POST":
        form = UserresetForm(request.POST)
        if form.is_valid():
            usera = request.POST['nombreusuario']
            user_validate = User.objects.get(username=usera)
            if not user_validate:
                return redirect('login')
            else:
                new_pass = get_random_string(length=32)
                user_validate.set_password(new_pass)
                user_validate.save()
                asunto = 'Su nueva contraseña desde el Ropero'
                mensaje = 'Aqui lo que solicitaste tu nueva contraseña es: ' + new_pass
                from_mail = settings.EMAIL_HOST_USER
                to = [user_validate.email, ]
                send_mail(asunto, mensaje, from_mail, to)
                return redirect('login')
        form = UserresetForm()
    return render(request, 'blog/user_reset.html', {'form': form})


def producto_new(request):
    data = {
        'form': ProductForm()
    }
    if request.user.is_staff:
        if request.method == "POST":
            formulario = ProductForm(request.POST, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                return redirect('galeria')
            data['form'] = formulario
        return render(request, 'blog/producto_nuevo.html', data)
    else:
        return redirect('galeria')
