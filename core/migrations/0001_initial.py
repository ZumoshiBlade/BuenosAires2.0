# Generated by Django 4.0.4 on 2022-06-07 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('codename', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('email', models.CharField(blank=True, max_length=254, null=True)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CompraProducto',
            fields=[
                ('id_compra', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_compra', models.DateField()),
            ],
            options={
                'db_table': 'compra_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'comuna',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(blank=True, max_length=200, null=True)),
                ('action_flag', models.IntegerField()),
                ('change_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField(blank=True, null=True)),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EstadoCompra',
            fields=[
                ('id_estado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'estado_compra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('n_tarjeta', models.BigIntegerField()),
                ('nombre_propietario', models.CharField(max_length=200)),
                ('apellido_propietario', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha_expiracion', models.DateField(blank=True, null=True)),
                ('codigo_seguridad', models.BigIntegerField()),
                ('rut_titular', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'metodo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('stock', models.BigIntegerField()),
                ('precio', models.BigIntegerField()),
                ('img', models.BinaryField(blank=True, null=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('telefono', models.BigIntegerField()),
                ('email', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_servicio', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=200)),
                ('precio', models.BigIntegerField()),
                ('tiene_confirmacion', models.CharField(max_length=1)),
                ('fecha', models.DateField()),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SolicitudServ',
            fields=[
                ('id_solicitud', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha_solicitud', models.DateField()),
            ],
            options={
                'db_table': 'solicitud_serv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id_tp', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tproducto', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'tipo_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id_ts', models.BigIntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipo_servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ubicacion',
            fields=[
                ('id_ubicacion', models.BigIntegerField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=200)),
                ('n_hogar', models.BigIntegerField()),
                ('adicional', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'db_table': 'ubicacion',
                'managed': False,
            },
        ),
    ]