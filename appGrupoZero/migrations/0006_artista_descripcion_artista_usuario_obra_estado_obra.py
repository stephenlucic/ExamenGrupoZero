# Generated by Django 4.2.1 on 2023-07-03 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appGrupoZero', '0005_obra_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='descripcion',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='artista',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='obra',
            name='estado_obra',
            field=models.IntegerField(choices=[[0, 'Creada'], [1, 'Aprobada'], [2, 'Rechazada']], default=0),
        ),
    ]