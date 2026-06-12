from django.urls import path
from . import views


urlpatterns = [
    path('iniciar_sesion/', views.inicio_sesion, name='iniciar_sesion'),
    path('registrarse/', views.crear_usuario, name='crear_usuario'),
    path('cerrar_sesion/', views.logout, name='cerrar_sesion'),

]
