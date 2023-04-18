from django.urls import path
from AppCoder import views

urlpatterns = [
    path('insertacurso/<nombre>/<comision>', views.curso),
    path('listacursos/', views.lista_cursos, name="Cursos"),
    path('', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('estudianteformulario/', views.estudianteFormulario, name="EstudianteFormulario"),
    path('profesores/', views.profesores, name="Profesores"),
    path('profesorformulario/', views.profesorFormulario, name="ProfesorFormulario"),
    path('entregables', views.entregables, name="Entregables"),
    path("busquedaComision", views.busquedaComision, name="BusquedaComision"),
    path('buscar/', views.buscar, name="Buscar"),
    
]
