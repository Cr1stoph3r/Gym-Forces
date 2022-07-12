from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('galeria', views.GaleriaViewset)

app_name='main'

urlpatterns = [
    path('index', views.index, name='index'),
    path('registro', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('contacto', views.contacto, name='contacto'),
    path('agregar-imagen',views.agregar_imagen, name="agregar_imagen"),
    path('modificar-imagen/<id>/', views.modificar_imagen, name="modificar_imagen"),
    path('listar-imagen',views.listar_imagen, name="listar_imagen"),
    path('eliminar-imagen/<id>/',views.eliminar_imagen, name="eliminar_imagen"),
    path('api/', include(router.urls)),
    path('error-facebook/', views.error_facebook, name="error_facebook")
]