# Generated by Django 5.0.4 on 2024-04-26 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FICHA', models.CharField(max_length=9)),
                ('TIPO_DE_DOCUMENTO', models.CharField(max_length=4, null=True)),
                ('NUMERO_DE_DOCUMENTO', models.CharField(max_length=10)),
                ('NOMBRE', models.CharField(max_length=150)),
                ('APELLIDOS', models.CharField(max_length=150)),
                ('CELULAR', models.CharField(max_length=10, null=True)),
                ('CORREO_ELECTRONICO', models.CharField(max_length=200)),
                ('ESTADO', models.CharField(max_length=50, null=True)),
                ('GRUPO', models.CharField(max_length=20)),
                ('HASH', models.CharField(max_length=50)),
                ('HASH_SEND', models.DateTimeField()),
                ('FECHA_DE_UPLOAD', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGIONAL', models.CharField(max_length=50, null=True)),
                ('CENTRO', models.CharField(max_length=50, null=True)),
                ('COORDINACION', models.CharField(max_length=50, null=True)),
                ('NOMBRE', models.CharField(max_length=150)),
                ('APELLIDOS', models.CharField(max_length=150)),
                ('EMAIL', models.CharField(max_length=200, null=True)),
                ('GRUPO', models.CharField(max_length=20)),
                ('HASH', models.CharField(max_length=50)),
                ('HASH_SEND', models.DateTimeField()),
                ('FECHA_DE_UPLOAD', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('REGIONAL', models.CharField(max_length=50, null=True)),
                ('CENTRO', models.CharField(max_length=50, null=True)),
                ('FECHA_LISTAS', models.DateTimeField()),
                ('FECHA_EVALUACION', models.DateTimeField()),
                ('FECHA_DE_SOLICITUD', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FICHA', models.CharField(max_length=9)),
                ('PROGRAMA_DE_FORMACION', models.CharField(max_length=200, null=True)),
                ('TIPO_DOCUMENTO', models.CharField(max_length=4, null=True)),
                ('NUMERO_DE_DOCUMENTO', models.CharField(max_length=10)),
                ('NOMBRE', models.CharField(max_length=150)),
                ('APELLIDOS', models.CharField(max_length=150)),
                ('PERFIL_DEL_INSTRUCTOR', models.CharField(max_length=200, null=True)),
                ('GRUPO', models.CharField(max_length=20)),
                ('HASH', models.CharField(max_length=50)),
                ('HASH_SEND', models.DateTimeField()),
                ('FECHA_DE_UPLOAD', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
