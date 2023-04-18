from django import forms
from .models import Entregable, Estudiante, Curso, Profesor
from django.forms import ModelForm


class CursoFormulario(ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'comision']


class ProfesorFormulario(ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'profesion']


class EntregableFormulario(ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'fecha_entrega', 'entregado']


class EstudianteFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email']
