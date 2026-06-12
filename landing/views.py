from django.shortcuts import render


def home(request):
    usuario_actual = request.session.get("logueado")
    
    if usuario_actual and usuario_actual.get("rol") == "admin":
        return render(request, 'landing/inicio_admin.html')
        
    return render(request, 'landing/landing.html')
