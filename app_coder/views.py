from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def curso(request):

    curso = Curso(4, 'Python', 31109 )
    curso.save()

    texto = f'curso creado nombre={curso.nombre} comision={curso.comision}'

    return HttpResponse(texto)

def inicio(request):
    return render(request, 'app_coder/inicio.html')

def cursos(request):
    return render(request, 'app_coder/cursos.html')

def estudiantes(request):
    return render(request, 'app_coder/estudiantes.html')

def profesores(request):
    return render(request, 'app_coder/profesores.html')

def entregables(request):
    return render(request, 'app_coder/entregables.html')
