from django.urls import path
from . import views

urlpatterns = [
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('crear-producto/', views.crear_producto, name='crear_producto'),
    path('crear-pedido/', views.crear_pedido, name='crear_pedido'),
    path('buscar-cliente/', views.buscar_cliente, name='buscar_cliente'),
]
