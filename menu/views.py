from django.shortcuts import render, redirect


def ver_carta(request):
    return render(request, "menu/carta.html")

def carta_admin(request):
    return render(request, "menu/menu_admin.html")

def crear_plato(request):
    if request.method == "POST":
        pass

