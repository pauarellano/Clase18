from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):
    nombre_curso="JS"
    comision_curso=12345

    curso=Curso(nombre=nombre_curso,comision=comision_curso)
    curso.save()
    respuesta=f"Curso creado--- {nombre_curso}- {comision_curso}"
    return HttpResponse(respuesta)

def cursos(request):

    return render(request,"Appcoder/cursos.html") #Crear URL

def profesores(request):

    return render (request,"Appcoder/profesores.html")#Crear URL

def estudiantes(request):

    return render (request,"Appcoder/estudiantes.html")#Crear URL

def entregables(request):

    return render(request,"Appcoder/entregables.html")#Crear URL

def inicio(request):
    return HttpResponse("Pagina de inicio")
def inicioApp(request):

    return render(request,"Appcoder/inicio.html")  