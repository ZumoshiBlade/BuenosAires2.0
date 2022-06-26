from django.db import connection
from django.shortcuts import redirect, render 
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required 
import cx_Oracle
import base64
import requests
from zeep import Client
# Create your views here.


def home(request):
    return render(request, 'core/home.html')

def productos(request):
    #Productos de ANWO
    
    #Productos Buenos Aires

    datos_productos=listar_productos()
    arreglo = []

    for i in datos_productos:
        if i[5]:
            data = {
            'data': i,
            'imagen': str(base64.b64encode(i[5].read()), 'utf-8'),
            }
        else:
            data = {
            'data': i,
            }
        arreglo.append(data)
        
    data = {
        'productos' : arreglo,
    }
    return render(request, 'core/productos.html', data)    

def detalle_producto(request, id):

    producto = ver_producto(id)
    arreglo = []

    for i in producto:
        if i[5]:
            data = {
            'data': i,
            'imagen': str(base64.b64encode(i[5].read()), 'utf-8'),
            }
        else:
            data = {
            'data': i,
            }
    arreglo.append(data)
    data = {
    'producto' : arreglo,
    }

    return render(request, 'core/detalle_producto.html', data)

@login_required
def sistema_pago(request, id):

    usuario = request.user.username

    data = {
        'tarjeta': listar_metodos_pago(usuario),
    }

    if request.method == 'POST':
        id_tarjeta = request.POST.get('tipo_pago')
        n_tarjeta = int(obtener_num_tarjeta(id_tarjeta))
        codigo = int(obtener_codigo(id_tarjeta))
        precio = int(precio_producto(id))

        cliente = Client("http://localhost:8080/WS_WebPay/WSPago?WSDL")
        resultado = cliente.service.Pago(n_tarjeta, codigo, precio)

        if resultado == 1:
            salida = add_compra(id, id_tarjeta, usuario)

            if salida > 0:
                messages.success(request, "¡Compra realizada!")
                return redirect(to="productos")
            else:
                messages.error(request, "¡Error al ingresar la compra del producto!")

        elif resultado == 2:
            messages.warning(request, "Saldo insuficiente")

        else:
            messages.error(request, "¡Error al conectarse con webpay!")


    return render(request, 'core/sistema_pago.html', data)

@login_required
def servicios(request):
    return render(request, 'core/servicios.html')

@login_required
def perfil(request):
    usuario = request.user.username
    compras = listar_compras(usuario)

    data = {
        'compras': compras,
    }
    

    return render(request, 'core/perfil.html', data)

@login_required
def metodo_pago(request):

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
            return redirect(to="list_mp")
        else:
            messages.warning(request, "No se ha podido agregar el metodo de pago :(")

    return render(request, 'metodo_pago/agregar_metodo_pago.html', data)

@login_required
def lista_metodo_pago(request):

    usuario = request.user.username

    data = {
        'tarjeta': listar_metodos_pago(usuario)
    }

    return render(request, 'metodo_pago/lista_metodo_pago.html', data)

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

def listar_productos():

    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista 

def listar_metodos_pago(usuario):
    django_cursor =  connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTA_MT_USER", [usuario, out_cur] )

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

def eliminar_metodo_pago(request,id):
    django_cursor =  connection.cursor()
    cursor = django_cursor.connection.cursor()
    cursor.callproc("SP_ELIMINAR_MP", [id])

    messages.success(request, "Eliminado correctamente")
    return redirect(to='list_mp')

def ver_producto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_VER_PRODUCTO", [id, out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista 

def add_compra(id_producto, id_tarjeta, id_user):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_COMPRA_PRODUCTO', [id_producto, id_tarjeta, id_user, salida])

    return salida.getvalue()

def precio_producto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_PRECIO', [id, salida])

    return salida.getvalue()

def obtener_num_tarjeta(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_N_TARJETA', [id, salida])

    return salida.getvalue()

def obtener_codigo(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc('SP_CODIGO', [id, salida])

    return salida.getvalue()

def listar_compras(usuario):
    django_cursor =  connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTA_COMPRAS", [usuario, out_cur] )

    lista = []

    for fila in out_cur:
        lista.append(fila)

    return lista

def seguimiento(request, id):
    cliente = Client("http://localhost:8080/WS_Seguimiento/WSSeguimiento?WSDL")
    respuesta = cliente.service.Seguimiento(id)

    if respuesta == 1:
        mensaje = "Su producto esta siendo despachado"
    elif respuesta == 2:
        mensaje = "Su producto va en camino"
    elif respuesta == 3:
        mensaje = "Su producto ya ha llegado"
    else:
        mensaje = "Error al capturar el seguimiento de su producto"


    data = {
        'respuesta': respuesta,
        'mensaje': mensaje
    }

    return render(request, 'core/seguimiento.html', data)