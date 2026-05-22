from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=50)
    #El unique = True Evita que 2 personas entren con el mismo correo
    email = models.EmailField(unique=True,max_length=100)
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.contraseña}"
