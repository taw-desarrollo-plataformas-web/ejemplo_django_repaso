from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext

# importar las clases de models.py
from educativa.models import Estudiante, Docente, Ciudad
# importar los formularios de forms.py
from educativa.forms import EstudianteForm


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

def crear_estudiante(request):
    """
    """
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(inicio)
    else:
        formulario = EstudianteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_estudiante.html', diccionario)

def editar_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    if request.method=='POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(inicio)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_estudiante.html', diccionario)
