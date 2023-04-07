from django.urls import path
from .views import * #Estas son del archivo de views dentro de la AppCoder


urlpatterns = [
    path("crearcurso/",crear_curso),
    path("cursos/",cursos),
    path("profesores/",profesores),
    path("estudiantes/",estudiantes),
    path("entregables/",entregables),
    path("",inicioApp),
]