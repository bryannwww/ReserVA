from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.ver_carta, name='ver_carta'),
    path('menu_admin/', views.carta_admin, name='carta_admin'),
]
