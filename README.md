# Buenos Aires 2.0

Plataforma de e-commerce para la venta e instalación de sistemas de aire acondicionado de la marca **ANWO**, desarrollada con Django 5.2 LTS.

---

## ¿Qué es?

Buenos Aires 2.0 es una aplicación web full-stack que permite a los usuarios explorar el catálogo de productos de climatización, solicitar servicios de instalación y mantenimiento, gestionar métodos de pago y realizar seguimiento de pedidos. Está diseñada para operar con base de datos Oracle en producción e integrarse con el servicio de pagos **WebPay** y un sistema de **seguimiento de envíos** vía SOAP.

---

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Python 3 + Django 5.2 LTS |
| Frontend | Bootstrap 5.3.3 + CSS personalizado |
| Base de datos | SQLite (desarrollo) / Oracle (producción) |
| Formularios | django-crispy-forms + crispy-bootstrap5 |
| Pagos | WebPay (integración SOAP con zeep) |
| Seguimiento | SOAP (zeep) |
| Driver Oracle | oracledb >= 2.0 |

---

## Estructura del proyecto

```
BuenosAires2.0/
├── BuenosAires/              # Configuración principal del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/                     # Aplicación principal
│   ├── models.py             # Modelos de base de datos
│   ├── views.py              # Lógica de vistas
│   ├── urls.py               # Rutas de la app
│   ├── forms.py              # Formularios
│   ├── admin.py              # Configuración del admin
│   ├── static/core/          # CSS e imágenes
│   └── templates/            # Plantillas HTML
├── manage.py
├── requirements.txt
└── db.sqlite3                # Base de datos de desarrollo
```

---

## Modelos principales

| Modelo | Descripción |
|---|---|
| `Producto` | Unidades de aire acondicionado (nombre, precio, stock, imagen) |
| `TipoProducto` | Categorías de productos |
| `Proveedor` | Proveedores/fabricantes |
| `CompraProducto` | Transacciones de compra |
| `EstadoCompra` | Estado del pedido (pendiente, despachado, entregado) |
| `MetodoPago` | Tarjetas de pago guardadas por el usuario |
| `TipoPago` | Tipos de pago (crédito, débito, etc.) |
| `Servicio` | Servicios de instalación y mantenimiento |
| `TipoServicio` | Tipos de servicio |
| `SolicitudServ` | Solicitudes de servicio |
| `Region` / `Comuna` | Datos geográficos |
| `Ubicacion` | Direcciones de los usuarios |

---

## Funcionalidades

- **Catálogo de productos**: listado con imágenes, precios y disponibilidad de stock
- **Detalle de producto**: vista individual con descripción completa
- **Registro e inicio de sesión**: autenticación con Django Auth
- **Perfil de usuario**: historial de compras y datos personales
- **Métodos de pago**: agregar, listar y eliminar tarjetas guardadas
- **Proceso de compra**: selección de método de pago y confirmación
- **Solicitud de servicios**: formulario para solicitar instalación o mantenimiento
- **Seguimiento de pedidos**: integración con servicio SOAP de tracking
- **Panel de administración**: gestión completa vía Django Admin

---

## Rutas disponibles

| URL | Vista | Descripción |
|---|---|---|
| `/` | `home` | Página principal |
| `/productos/` | `productos` | Catálogo de productos |
| `/detalle_producto/<id>/` | `detalle_producto` | Detalle de un producto |
| `/servicios/` | `servicios` | Listado de servicios |
| `/registro/` | `registro` | Registro de usuario |
| `/perfil/` | `perfil` | Perfil del usuario autenticado |
| `/agregar_metodo_pago/` | `metodo_pago` | Agregar método de pago |
| `/lista_metodo_pago/` | `lista_metodo_pago` | Ver métodos de pago guardados |
| `/eliminar_metodo_pago/<id>/` | `eliminar_metodo_pago` | Eliminar un método de pago |
| `/sistema_pago/<id>/` | `sistema_pago` | Proceso de pago de un producto |
| `/seguimiento/<id>/` | `seguimiento` | Seguimiento de un pedido |
| `/admin/` | Django Admin | Panel de administración |

---

## Instalación y configuración

### Requisitos previos

- Python 3.10+
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone <url-del-repositorio>
cd BuenosAires2.0

# 2. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (para acceder al admin)
python manage.py createsuperuser

# 6. Ejecutar el servidor de desarrollo
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000/`.

---

## Configuración de base de datos

### SQLite (por defecto, desarrollo)

No requiere configuración adicional. El archivo `db.sqlite3` se genera automáticamente.

### Oracle (producción)

En `BuenosAires/settings.py`, reemplazar la configuración de base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'system',
        'USER': 'buenosaires',
        'PASSWORD': 'buenosaires',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}
```

---

## Integraciones SOAP

### WebPay (pagos)

Endpoint esperado: `http://localhost:8080/WS_WebPay/WSPago?WSDL`

### Seguimiento de envíos

Endpoint esperado: `http://localhost:8080/WS_Seguimiento/WSSeguimiento?WSDL`

> Ambas integraciones están implementadas con stubs y se activan una vez que los servicios SOAP externos estén disponibles.

---

## Variables de entorno recomendadas para producción

| Variable | Descripción |
|---|---|
| `SECRET_KEY` | Clave secreta de Django (reemplazar la por defecto) |
| `DEBUG` | Establecer en `False` en producción |
| `ALLOWED_HOSTS` | Lista de hosts permitidos |
| `DB_USER` / `DB_PASSWORD` | Credenciales de Oracle |

---

## Dependencias

```
Django>=5.2,<5.3
oracledb>=2.0
django-crispy-forms>=2.3
crispy-bootstrap5>=2024.10
zeep>=4.2
```

---

## Notas de desarrollo

- Las imágenes de productos se almacenan codificadas en base64 en la base de datos.
- Todas las vistas de usuario requieren autenticación (`@login_required`), excepto home, productos y registro.
- El proyecto fue migrado a Django 5.2 LTS desde una versión anterior.
