from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductosApi, imagenesAPI
from rest_framework import routers

router = routers.DefaultRouter()
router.register('productos', ProductosApi)
router.register('imagenes', imagenesAPI)


urlpatterns = [
    path('galeria', views.galeria, name='galeria'),
    path('', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('producto_new', views.producto_new, name='ingreso_producto'),
    path('producto/<int:pk>/edit/', views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/del/', views.producto_del, name='producto_del'),
    path('user_reset', views.user_reset, name='user_reset'),
    path('api/', include(router.urls)),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
