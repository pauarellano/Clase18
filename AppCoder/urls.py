from django.urls import path
from .views import * #Estas son del archivo de views dentro de la AppCoder


urlpatterns = [
    path("crearcurso/",crear_curso),
    path("cursos/",cursos,name="cursos"),
    path("profesores/",profesores,name="profesores"),
    path("estudiantes/",estudiantes, name="estudiantes"),
    path("entregables/",entregables,name="entregables"),
    path("",inicioApp,name="inicioApp"),
]