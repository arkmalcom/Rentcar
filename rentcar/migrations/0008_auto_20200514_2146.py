# Generated by Django 3.0.6 on 2020-05-15 01:46

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0007_auto_20200514_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='fecha_ingreso',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='Inspeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ralladuras', models.BooleanField()),
                ('porcentaje_combustible', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('goma_repuesto', models.BooleanField()),
                ('gato', models.BooleanField()),
                ('roturas_cristal', models.BooleanField()),
                ('goma_uno', models.BooleanField()),
                ('goma_dos', models.BooleanField()),
                ('goma_tres', models.BooleanField()),
                ('goma_cuatro', models.BooleanField()),
                ('inspeccion_fecha', models.DateField(auto_now_add=True)),
                ('estado', models.BooleanField()),
                ('inspeccion_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar.Cliente')),
                ('inspeccion_empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar.Empleado')),
                ('inspeccion_vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentcar.Vehiculo')),
            ],
        ),
    ]
