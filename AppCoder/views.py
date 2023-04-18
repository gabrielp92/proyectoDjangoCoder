from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso, Estudiante, Entregable, Profesor
from .forms import ProfesorFormulario, EstudianteFormulario, EntregableFormulario
#from datetime import datetime

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
    lista_estudiantes = Estudiante.objects.all()
    return render(self, "estudiantes.html", {"estudiantes": lista_estudiantes})
  
def profesores(self):
    lista_profesores = Profesor.objects.all()
    return render(self, "profesores.html", {"profesores": lista_profesores})

def entregables(self):
    lista_entregables = Entregable.objects.all()
    return render(self, "entregables.html", {"entregables": lista_entregables})

def buscar(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        curso = Curso.objects.filter(nombre__icontains=nombre)
        print(curso)
        return render(request, 'inicio.html', {"cursos": curso})


def busquedaComision(request):
    return render(request, 'busquedaComision.html')

def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            print(data)
            estudiante = Estudiante(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            estudiante.save()
            lista_estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes.html', {"estudiantes": lista_estudiantes})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario})

def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            profesor.save()
            lista_profesores = Profesor.objects.all()
            return render(request, 'profesores.html', {"profesores": lista_profesores})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})

def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            entregable = Entregable(
                nombre=data['nombre'], fecha_entrega=data['fecha_entrega'], entregado=data['entregado'])
            entregable.save()
            lista_entregables = Entregable.objects.all()
            return render(request, 'entregables.html', {"entregables": lista_entregables})
        else:
            return HttpResponse('<script>alert("Datos de formulario invalidos")</script>')
    else:
        miFormulario = EntregableFormulario()
        return render(request, "entregableFormulario.html", {"miFormulario": miFormulario})