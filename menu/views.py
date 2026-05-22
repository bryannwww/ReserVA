from django.shortcuts import render, redirect


def ver_carta(request):
    return render(request, "menu/carta.html")
