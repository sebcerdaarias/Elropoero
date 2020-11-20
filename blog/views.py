from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import *
from .models import Post, imagenes, Productos
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, ProductForm
from django.shortcuts import redirect

from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def home(request):
    return render(request, 'blog/home.html')


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

def Producto_new(request):
    data = {
        'form':ProductForm()
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




