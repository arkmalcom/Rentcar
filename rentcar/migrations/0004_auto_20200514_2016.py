# Generated by Django 3.0.6 on 2020-05-15 00:16

from django.db import migrations, models
import django.db.models.deletion
import rentcar.validators
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0003_tipocombustible_vehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('cedula', models.CharField(max_length=13, validators=[rentcar.validators.validate_cedula])),
                ('limite_credito', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tipo_persona', models.CharField(choices=[('F', 'Fisica'), ('J', 'Juridica')], max_length=100)),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='modelo_vehiculo',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='marca_vehiculo', chained_model_field='marca', on_delete=django.db.models.deletion.CASCADE, to='rentcar.Modelo'),
        ),
    ]
