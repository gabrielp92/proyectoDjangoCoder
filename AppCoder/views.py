from django.shortcuts import render
from django.http import HttpResponse
#from django.template import Template, Context, loader
#from datetime import datetime
from .models import Curso, Estudiante, Entregable, Profesor

def inicio(self):
    return render(self, "inicio.html") 

def curso(self, nombre, comision):
    nuevo_curso = Curso(nombre=nombre, comision=comision)
    nuevo_curso.save()
    return render(self, "cursos.html")

def lista_cursos(self):
    lista = Curso.objects.all()
    return render(self, "lista_cursos.html", {"lista_cursos": lista})
    
def estudiantes(self):
    return render(self, "estudiantes.html")    
    
def profesores(self):
    return render(self, "profesores.html") 

def entregables(self):
    return render(self, "entregables.html") 

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        curso = Curso.objects.filter(nombre__icontains=nombre)
        print(curso)
        return render(request, 'inicio.html', {"cursos": curso})


def busquedaComision(request):
    return render(request, 'busquedaComision.html')
