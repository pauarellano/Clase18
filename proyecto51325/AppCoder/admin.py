from django.contrib import admin

# Register your models here.
from .models import Curso,Profesor,Estudiante,Entregable

admin.site.register(Curso)  
admin.site.register(Profesor)  
admin.site.register(Estudiante)  
admin.site.register(Entregable)  
