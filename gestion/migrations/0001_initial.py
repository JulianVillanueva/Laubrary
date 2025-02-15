# Generated by Django 5.1 on 2024-09-20 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('autor', models.TextField()),
                ('anio_publicacion', models.IntegerField()),
                ('genero', models.CharField(max_length=255)),
                ('num_copias', models.IntegerField()),
                ('estado', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_prestatario', models.CharField(max_length=255)),
                ('fecha_devolucion_real', models.DateField(blank=True, null=True)),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamo', to='gestion.libro')),
            ],
        ),
        migrations.CreateModel(
            name='RecordatorioDevolucion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recordatorio_enviado', models.BooleanField(default=False)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RecordatorioDevolucion', to='gestion.prestamo')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('prestamos_realizados', models.IntegerField()),
                ('libro_mas_solicitado', models.ManyToManyField(related_name='Reporte', to='gestion.libro')),
            ],
        ),
    ]
