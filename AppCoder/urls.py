from django.urls import path
from AppCoder import views

urlpatterns = [
    path('insertacurso/<nombre>/<comision>', views.curso),
    path('listacursos/', views.lista_cursos, name="Cursos"),
    path('', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores"),
    path('entregables', views.entregables, name="Entregables")
]
