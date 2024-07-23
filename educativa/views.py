from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from educativa.models import Estudiante, Docente


def inicio(request):
    """
    """

    return render(request, 'inicio.html')

def listar_estudiantes(request):
    """
    """
    estudiantes = Estudiante.objects.all()
    numero_estudiantes = len(estudiantes)

    informacion_template = {'estudiantes': estudiantes,
        'numero_estudiantes': numero_estudiantes}
    return render(request, 'listar_estudiantes.html', informacion_template)

def listar_docentes(request):
    """
    """
    docentes = Docente.objects.all()
    numero_docentes = len(docentes)

    informacion_template = {'docentes': docentes,
        'numero_docentes': numero_docentes}
    return render(request, 'listar_docentes.html', informacion_template)
