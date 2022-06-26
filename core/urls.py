from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.productos, name="productos"),
    path('detalle_producto/<id>/', views.detalle_producto, name="detalle_producto"),
    path('servicios/', views.servicios, name="servicios"),
    path('registro/',views.registro, name="registro"),
    path('perfil/',views.perfil, name="perfil"),
    path('agregar_metodo_pago/',views.metodo_pago, name="add_mp"),
    path('lista_metodo_pago/', views.lista_metodo_pago, name="list_mp"),
    path('eliminar_metodo_pago/<id>/', views.eliminar_metodo_pago, name="delete_mp"),
    path('sistema_pago/<id>/',views.sistema_pago, name="sistema_pago"),
    path('seguimiento/<id>/', views.seguimiento, name="seguimiento")
]