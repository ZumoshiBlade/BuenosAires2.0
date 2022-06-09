from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('productos/', views.productos, name="productos"),
    path('servicios/', views.servicios, name="servicios"),
    path('registro/',views.registro, name="registro")
]