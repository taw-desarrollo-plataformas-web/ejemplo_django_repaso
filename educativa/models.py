from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return "Ciudad: %s - Región: %s" % (self.nombre, self.region)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,
            related_name="estudiantes_ciudad")

    def __str__(self):
        return "Estudiante: %s - %s - %s - ciudad (%s)" % (
            self.nombre,
            self.apellido,
            self.correo,
            self.ciudad)

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    titulo = models.CharField(max_length=200)
    contrato = models.CharField(max_length=200)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE,
            related_name="docentes_ciudad")

    def __str__(self):
        return "Docente: %s - %s - %s - ciudad (%s)" % (
            self.nombre,
            self.titulo,
            self.contrato,
            self.ciudad)
