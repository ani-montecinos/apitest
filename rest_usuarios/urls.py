from django.urls import path
from rest_usuarios.views import *


urlpatterns = [
    path('users',listar_usuarios,name="lista_usuarios"),
    path('usuario/<id>',mostrar_usuario,name="usuario"),

]