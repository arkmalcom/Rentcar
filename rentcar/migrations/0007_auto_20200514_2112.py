# Generated by Django 3.0.6 on 2020-05-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcar', '0006_auto_20200514_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='imagen',
            field=models.ImageField(default='placeholder.jpg', upload_to='img/vehiculos'),
        ),
    ]