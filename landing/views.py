from django.shortcuts import render


def home(request):  #funcion casa, como siempre estara en home se ejecuta siempre el return
    return render(request, 'landing/landing.html')
#devuelve el render que sera el landing
