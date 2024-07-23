from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    def __str__(self):
        return "Estudiante: %s - %s - %s" % (
            self.nombre,
            self.apellido,
            self.correo)

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    titulo = models.CharField(max_length=200)
    contrato = models.CharField(max_length=200)

    def __str__(self):
        return "Docente: %s - %s - %s" % (
            self.nombre,
            self.titulo,
            self.contrato)
