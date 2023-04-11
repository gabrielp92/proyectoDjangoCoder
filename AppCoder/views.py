from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime

def saludo(request):
    return HttpResponse("Hola django - Coder")

def segunda_view(request):
    return HttpResponse("""
    <h1>Bienvenidos!!!</h1>
    <br>
    <p><i>sitio hecho con django y python</i></p>
    """)

def dia_de_hoy(request):
    dia = datetime.now()
    mensaje = f"Hoy es día: <br> <b>{dia}</b>"
    return HttpResponse(mensaje)

def saluda_con_nombre(request, nombre):
    mensaje = f"<h2>Saludos para <b>{nombre}</b> !!!</h2>"
    return HttpResponse(mensaje)

def probando_template(request):
    #mi_html = open("C:/Users/usuario/Desktop/Python/pythonConDjango/proyectoPythonDjango/proyectoPythonDjango/templates/template1.html")
    plantilla = loader.get_template('template1.html')
    lista_notas = [67,81,53,74,62,94,41,86]
    diccionario = {
        "name": "Gabriel",
        "notas": lista_notas
    }
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)