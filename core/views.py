from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def login(request):
    return render(request, 'core/login.html')