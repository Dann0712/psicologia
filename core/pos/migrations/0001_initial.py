# Generated by Django 4.0.2 on 2024-05-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=150, verbose_name='Nombres')),
                ('telefono', models.CharField(blank=True, max_length=10, null=True, verbose_name='Teléfono')),
                ('correo_electronico', models.CharField(blank=True, max_length=50, null=True, verbose_name='Correo electrónico')),
                ('fecha_cita', models.DateField(verbose_name='Fecha de la cita')),
                ('hora_cita', models.TimeField(verbose_name='Hora de la cita')),
                ('psicologo', models.CharField(max_length=150, verbose_name='Psicólogo')),
                ('proposito', models.TextField(verbose_name='Propósito de la cita')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
            },
        ),
    ]
