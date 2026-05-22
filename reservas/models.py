from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()
    telefono = models.CharField(max_length=20)
    mesa = models.CharField(max_length=3)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"