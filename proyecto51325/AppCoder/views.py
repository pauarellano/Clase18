from django.shortcuts import render
from .models import Curso,Profesor #Se importa el profesor Clase 21. 
from django.http import HttpResponse
from .forms import ProfesorForm #Clase 21

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

    if request.method=="POST":
        form= ProfesorForm(request.POST)

        if form.is_valid():
            nombre=form.cleaned_data["nombre"]
            apellido=form.cleaned_data["apellido"]
            email=form.cleaned_data["email"]
            profesion=form.cleaned_data["profesion"]
            profesor=Profesor() #Crea un objeto tipo profesor
            profesor.nombre=nombre #variable de arriba que se acaba de crear
            profesor.apellido=apellido
            profesor.email=email
            profesor.profesion=profesion
            profesor.save() 
            form=ProfesorForm() #Se crea el formulario en html
        
        else:
            pass #No es necesario en el código. 
    else:
        form=ProfesorForm() #En el contexto agregaremos una entrada "form"

    profesores=Profesor.objects.all #Creará una lista de objetos en este modelo, para mostrar una lista de profesores en html
    context={"profesores":profesores,"form":form} #Clase 21, se agrega el contexto y se lleva al render

    return render (request,"Appcoder/profesores.html",context)#Crear URL

def estudiantes(request):

    return render (request,"Appcoder/estudiantes.html")#Crear URL

def entregables(request):

    return render(request,"Appcoder/entregables.html")#Crear URL

def inicio(request):
    return HttpResponse("Pagina de inicio")
def inicioApp(request):

    return render(request,"Appcoder/inicio.html")  