from django.shortcuts import render, redirect
from .models import Resena
from django.http import HttpResponse
from usuarios.decorador import verificar
@verificar
def crear_resena(request):
    if request.method == "POST":
        comida = request.POST.get("comida")
        servicio = request.POST.get("servicio")
        comentario = request.POST.get("comentario")

        Resena.objects.create(
            usuario=request.user,
            calificacion_comida=comida,
            calificacion_servicio=servicio,
            comentario=comentario
        )

        return HttpResponse("Reseña enviada con éxito")

    return render(request, "comentarios/resena.html")