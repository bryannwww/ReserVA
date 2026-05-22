from django.urls import path
from . import views
app_name = 'comentarios'

urlpatterns = [
    path('resenas/', views.crear_resena, name='nueva_resena'),
]
