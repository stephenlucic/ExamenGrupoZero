# Generated by Django 4.2.1 on 2023-06-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appGrupoZero', '0002_artista_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150)),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'sugerencias'], [1, 'reclamos'], [2, 'consultas']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]