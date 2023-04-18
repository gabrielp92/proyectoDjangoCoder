from django.urls import path
from AppCoder import views

urlpatterns = [
    path('insertacurso/<nombre>/<comision>', views.curso),
    path('listacursos/', views.lista_cursos),
    path('', views.inicio),
    path('estudiantes/', views.estudiantes),
    path('profesores/', views.profesores),
    path('entregables', views.entregables)
]
