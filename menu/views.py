from django.shortcuts import render, redirect


def ver_carta(request):
    return render(request, "menu/carta.html")

def ver_carta(request):
    # 1. Por defecto, asumimos que es un cliente normal
    plantilla_base = 'base.html'
    
    # 2. Si hay sesión iniciada y el rol es 'admin', cambiamos la plantilla
    if request.session.get('logueado', {}).get('rol') == 'admin':
        plantilla_base = 'base_admin.html'
    
    # Aquí puedes tener lógica extra si traes los platos de la base de datos...
    
    # 3. Pasamos 'base_template' dentro del diccionario de contexto
    return render(request, 'nombre_de_tu_html_de_la_carta.html', {
        'base_template': plantilla_base
    })
