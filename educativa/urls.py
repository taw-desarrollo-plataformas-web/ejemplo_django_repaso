"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
        path('', views.inicio, name='inicio'),
        path('ver/estudiantes', views.listar_estudiantes,
            name='listar_estudiantes'),
        path('ver/docentes', views.listar_docentes,
            name='listar_docentes'),

 ]
