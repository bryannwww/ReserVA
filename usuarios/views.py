from django.shortcuts import render, redirect
from django.contrib import messages
from usuarios.models import Usuario

def inicio_sesion(request):
    if request.method == "POST":
        # Creamos una variable que atrapa lo que viene en el HTML
        usuario_html = request.POST.get("usuario")
        clave_html = request.POST.get("contraseña")

        try:
            # Acá hacemos un query para ver si coincide con la BD
            q = Usuario.objects.get(usuario=usuario_html, contraseña=clave_html)

            # Guardamos la manilla en el maletín (Sesión)
            request.session["logueado"] = {
                "id": q.id,
                "nombre": q.nombre,
            }

            return redirect('inicio')

        except Usuario.DoesNotExist:

            request.session["logueado"] = None
            messages.error(request, "Usuario o contraseña incorrectos")
            return redirect('iniciar_sesion')


    return render(request, "login.html")

def logout(request):
    try:
        del request.session["logueado"]
        return redirect('inicio')
    except Exception as e:
        return redirect('inicio')


def crear_usuario(request):
    if request.method == "POST":
        # Obtenemos los datos del formulario
        usuario = request.POST.get("usuario")
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email")
        contraseña = request.POST.get("contraseña")

        Usuario.objects.create(
            usuario=usuario,
            nombre=nombre,
            apellido=apellido,
            email=email,
            contraseña=contraseña,
        )
        return redirect('iniciar_sesion')

    # Arreglado: Limpiamos el error de sintaxis que se mezcló aquí abajo
    return render(request, "register.html")