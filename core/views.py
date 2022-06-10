from email import message
from django.db import connection
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import User
import cx_Oracle
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def productos(request):
    return render(request, 'core/productos.html')

@login_required
def servicios(request):
    return render(request, 'core/servicios.html')

@login_required
def perfil(request):
    return render(request, 'core/perfil.html')

@login_required
def agregar_metodo_pago(request):

    data={
        'tipo_pago':listado_tpago()
    }

    if request.method == 'POST':
        num_tarjeta = request.POST.get('numero_tarjeta')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_exp = request.POST.get('fecha_expiracion')
        codigo_seg = request.POST.get('codigo_seguridad')
        rut = request.POST.get('rut')
        tipo_pago = request.POST.get('tipo_pago')
        usuario = request.user.username
        salida = add_metodo_pago(num_tarjeta, nombre, apellido, fecha_exp, codigo_seg, rut, tipo_pago, usuario)

        if salida == 1:
            messages.success(request, "¡Metodo de pago agregado!")
            return redirect(to="perfil")
        else:
            messages.warning(request, "No se ha podido agregar el metodo de pago :(")

    return render(request, 'core/add_metodo_pago.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "¡Te has registrado correctamente!")
            return redirect(to="home")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)


def add_metodo_pago(num_tarjeta, nombre, apellido, fecha_exp, codigo_seg, rut, id_tp, id_user):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_AGREGAR_METODO_PAGO', [num_tarjeta, nombre, apellido, fecha_exp, codigo_seg, rut, id_tp, id_user, salida])

    return salida.getvalue()

def listado_tpago():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_TIPO_PAGO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista