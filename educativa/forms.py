from django.forms import ModelForm
from django import forms

from educativa.models import Estudiante, \
        Docente, Ciudad

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'correo', 'ciudad']
        widgets = {
                'nombre': forms.TextInput(attrs={
                    'class': 'control',
                    'placeholder': 'Ej: Ana Pérez'
                }),
                'apellido': forms.TextInput(attrs={
                    'class': 'control',
                    'placeholder': 'Ej: Pérez'
                }),
                'correo': forms.EmailInput(attrs={
                    'class': 'control',
                    'placeholder': 'Ej: ana@correo.com'
                }),
            }
