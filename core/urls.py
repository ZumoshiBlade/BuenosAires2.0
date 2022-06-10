from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.productos, name="productos"),
    path('servicios/', views.servicios, name="servicios"),
    path('registro/',views.registro, name="registro"),
    path('perfil/',views.perfil, name="perfil"),
    path('agregar_metodo_pago/',views.agregar_metodo_pago, name="add_mp"),
]