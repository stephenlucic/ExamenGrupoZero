# Generated by Django 4.2.1 on 2023-06-26 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGrupoZero.tipo')),
            ],
        ),
    ]