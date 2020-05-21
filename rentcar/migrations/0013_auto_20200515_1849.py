# Generated by Django 3.0.6 on 2020-05-15 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0012_auto_20200515_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='renta',
            name='estado',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='renta',
            name='vehiculo',
            field=models.ForeignKey(limit_choices_to={'estado': True}, on_delete=django.db.models.deletion.CASCADE, to='rentcar.Vehiculo'),
        ),
    ]