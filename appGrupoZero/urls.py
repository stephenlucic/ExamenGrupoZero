from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home, name="home"),
    path('', home, name = "home"),
    path('contacto', contacto, name="contacto"),
    path('artista', artista, name="artista"),
    path('galeria',galeria,name="galeria"),
    path('postular',postular,name="postular"),
    path('obras/<pk>/', obras , name= "obras"),
    path('desartista', desartista , name="desartista" ),
    path('agregar_artista/',agregar_artista, name="agregar_artista"),
    path('listar_artista/', listar_artista, name="listar_artista"),
    path('modificar_artista/<rutbuscado>/', modificar_artista, name="modificar_artista"),   
    path('eliminar_artista/<rutbuscado>/', eliminar_artista, name="eliminar_artista"),  
    path('login_usuario/', login_usuario, name="login_usuario"), 
    path('registro/', registro , name="registro"), 
    path('agregar_obra/', agregar_obra,name="agregar_obra"),
    path('listar_obra/', listar_obra, name="listar_obra"),
    path('modificar_obra/<codigobuscado>/',modificar_obra,name="modificar_obra"),
    path('eliminar_obra/<codigobuscado>/',eliminar_obra,name="eliminar_obra"),
    path('listar_postulantes',listar_postulantes,name="listar_postulantes"),
    path('eliminar_postulante/<rutbuscado>/',eliminar_postulante,name="eliminar_postulante")
 
]