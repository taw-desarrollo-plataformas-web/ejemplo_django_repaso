from django.forms import ModelForm
from django import forms

from educativa.models import Estudiante, \
        Docente, Ciudad

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'correo', 'ciudad']
