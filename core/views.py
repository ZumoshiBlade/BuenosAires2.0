from email import message
from urllib import response
from django.db import connection
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import User
import cx_Oracle
from zeep import Client
import base64
# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def productos(request):
    datos_productos=listar_productos()

    arreglo = []

    for i in datos_productos:
        if i[5]:
            data = {
            'data': i,
            'imagen': str(base64.b64encode(i[5].read()), 'utf-8')
            }
        else:
            data = {
            'data': i,
            }
        arreglo.append(data)
        
    data = {
        'productos' : arreglo
    }

    return render(request, 'core/productos.html', data)

@login_required
def servicios(request):
    client = Client('http://localhost:8080/WS_WebPay/WS_Pago?WSDL')

    data={
        'metodo_pago': listado_ppago(request.user.username),
        'servicios': listado_servicio()
    }
    
    if request.method == 'POST':
        servicio = request.POST.get('servicios')
        metodo_pago = request.POST.get('metodo_pago')
        usuario = request.user.username
        numero = numero_tarjeta(metodo_pago)
        precio = precio_servicio(servicio)
        saldo = saldo_tarjeta(numero)
        
        resultado = client.service.ProcesarPago(saldo, precio)
        if resultado <= 0:
            salida1 = solicitar_servicio(usuario, servicio, metodo_pago)

            #El saldo del cliente se actualiza pero siempre queda en 0
            salida2 = descuento_saldo(numero, resultado)
            if salida1 == 1:
                if salida2 == 1:
                    messages.success(request, "¡Servicio solicitado!")
                    return redirect(to="home")
                else:
                    messages.warning(request, "No se ha podido registrar la solicitud")
            else:
                messages.warning(request, "No se ha podido solicitar el servicio")
        else:
            messages.warning(request, "No tienes saldo suficiente")


    return render(request, 'core/servicios.html', data)

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

def descuento_saldo(id_metodo_pago, resultado):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_ACTUALIZAR_SALDO', [id_metodo_pago, resultado, salida])

    return salida.getvalue()

def solicitar_servicio(id_user, servicio, metodo_pago):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)   

    cursor.callproc('SP_SOLICITAR_SERVICIO', [id_user, servicio, metodo_pago, salida])  

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

def listado_ppago(username):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_METODO_PAGO", [username , out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista  

def listado_servicio():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_SERVICIO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista 

def precio_servicio(id_servicio):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_PRECIO_SERVICIO', [id_servicio, salida])  

    return salida.getvalue()

def saldo_tarjeta(numero_tarjeta):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_SALDO_TARJETA', [numero_tarjeta, salida])  

    return salida.getvalue()

def numero_tarjeta(id_metodo_pago):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_NUMERO_TARJETA', [id_metodo_pago, salida])  

    return salida.getvalue()

def listar_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista 