from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('post_list', views.post_list, name='post_list'),
    path('galeria', views.galeria, name='galeria'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('', views.index, name='index'),

    #path('welcome', views.welcome name='welcome'),
    #path('login', views.login name='login'),
    #path('register', views.register name='register),
    #path('logout', views.logout name='logout'),

   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
