from django.db import models

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField()
    telefono = models.CharField(max_length=20)
    mesa = models.CharField(max_length=3)
    notas = models.TextField(blank=True)
    ESTADOS_RESERVA = [
        ('pendiente', 'PENDIENTE'),
        ('asistio', 'ASISTIO'),
        ('cancelada', 'CANCELADA'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADOS_RESERVA, default='pendiente')

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"
    
class Plato(models.Model):
    nombre_plato = models.CharField(max_length=100)
    descripcion_plato = models.TextField(blank=False)
    precio_plato = models.IntegerField()
    def __str__(self):
        return f"{self.nombre_plato} - {self.precio_plato}"


class PlatoReserva(models.Model):
    reserva = models.ForeignKey('Reserva', on_delete=models.CASCADE, related_name='platos_pedidos')
    plato = models.ForeignKey(Plato, on_delete= models.CASCADE)
    cantidad = models.PositiveBigIntegerField(default=1)
    def __str__(self):
        return f"{self.cantidad}x {self.plato.nombre} (Reserva #{self.reserva.id})"
    
