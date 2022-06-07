# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CompraProducto(models.Model):
    id_compra = models.BigIntegerField(primary_key=True)
    fecha_compra = models.DateField()
    id_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='id_producto')
    id_metodo = models.ForeignKey('MetodoPago', models.DO_NOTHING, db_column='id_metodo')
    id_estado = models.ForeignKey('EstadoCompra', models.DO_NOTHING, db_column='id_estado')
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'compra_producto'


class Comuna(models.Model):
    id_comuna = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EstadoCompra(models.Model):
    id_estado = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'estado_compra'


class MetodoPago(models.Model):
    id_metodo = models.BigIntegerField(primary_key=True)
    n_tarjeta = models.BigIntegerField()
    nombre_propietario = models.CharField(max_length=200)
    apellido_propietario = models.CharField(max_length=200, blank=True, null=True)
    fecha_expiracion = models.DateField(blank=True, null=True)
    codigo_seguridad = models.BigIntegerField()
    rut_titular = models.CharField(max_length=200)
    id_tp = models.ForeignKey('TipoPago', models.DO_NOTHING, db_column='id_tp')
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    stock = models.BigIntegerField()
    precio = models.BigIntegerField()
    img = models.BinaryField(blank=True, null=True)
    id_tproducto = models.ForeignKey('TipoProducto', models.DO_NOTHING, db_column='id_tproducto')
    id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='id_proveedor')

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    telefono = models.BigIntegerField()
    email = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'proveedor'


class Region(models.Model):
    id_region = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'region'


class Servicio(models.Model):
    id_servicio = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    precio = models.BigIntegerField()
    tiene_confirmacion = models.CharField(max_length=1)
    fecha = models.DateField()
    id_ts = models.ForeignKey('TipoServicio', models.DO_NOTHING, db_column='id_ts')

    class Meta:
        managed = False
        db_table = 'servicio'


class SolicitudServ(models.Model):
    id_solicitud = models.BigIntegerField(primary_key=True)
    fecha_solicitud = models.DateField()
    id_servicio = models.ForeignKey(Servicio, models.DO_NOTHING, db_column='id_servicio')
    id_metodo = models.ForeignKey(MetodoPago, models.DO_NOTHING, db_column='id_metodo')
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'solicitud_serv'


class TipoPago(models.Model):
    id_tp = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_pago'


class TipoProducto(models.Model):
    id_tproducto = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'tipo_producto'


class TipoServicio(models.Model):
    id_ts = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_servicio'


class Ubicacion(models.Model):
    id_ubicacion = models.BigIntegerField(primary_key=True)
    calle = models.CharField(max_length=200)
    n_hogar = models.BigIntegerField()
    adicional = models.CharField(max_length=300, blank=True, null=True)
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_user = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_user')

    class Meta:
        managed = False
        db_table = 'ubicacion'
