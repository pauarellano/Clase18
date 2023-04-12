from django import forms

class ProfesorForm(forms.Form): #Lo siguiente proviene de models.py y se cambia el "model" por forms
    nombre=forms.CharField(max_length=50) #El label puede agregarse con otro nombre, sino lo determina como "nombre" así como el objeto.
    #Para cambiarlo es nombre=forms.CharField(max_length=50, label="Nombre del profesor")
    #Campo extra nombre=forms.CharField(max_length=50, label="Nombre del profesor", help_text="Ingrese el nombre del profe") Se pone al lado del campo
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField()
    profesion=forms.CharField(max_length=50)
