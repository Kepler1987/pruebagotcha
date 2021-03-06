# Generated by Django 2.1.1 on 2018-09-17 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Titulo')),
                ('equipo', models.CharField(max_length=250, verbose_name='Equipo')),
                ('bolas', models.IntegerField(verbose_name='Balas')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('valido', models.CharField(max_length=100, verbose_name='Valides')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'paquete',
                'verbose_name_plural': 'paquetes',
                'ordering': ['created'],
            },
        ),
    ]
