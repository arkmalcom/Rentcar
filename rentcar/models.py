from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from .validators import validate_cedula
from .validators import validate_cc
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.safestring import mark_safe

TIPO_PERSONA = (('F', 'Fisica'), ('J', 'Juridica'))
TANDAS = (('M', 'Matutina'), ('V', 'Vespertina'), ('N', 'Nocturna'))

class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Tipos de vehiculos"       

class Marca(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion

class TipoCombustible(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField()

    def __str__(self):
        return self.descripcion
    class Meta:
        verbose_name_plural = "Tipos de combustible"       

class Vehiculo(models.Model):
    descripcion = models.CharField(max_length=200)
    no_chasis = models.CharField(max_length=17)
    no_motor = models.CharField(max_length=9)
    no_placa = models.CharField(max_length=10)
    tipo_vehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.CASCADE)
    marca_vehiculo = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo_vehiculo = ChainedForeignKey(
        Modelo,
        chained_field="marca_vehiculo",
        chained_model_field="marca",
        show_all=False
    )
    combustible_vehiculo = models.ForeignKey(TipoCombustible, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img/vehiculos', default='placeholder.jpg')
    estado = models.BooleanField()

    def image_tag(self):
        return mark_safe('<img src="%s" style="width: 300px; height:200px;" />' % self.imagen.url)
    image_tag.short_description = 'Imagen'

    def __str__(self):
        return self.descripcion

class Cliente(models.Model):
    nombre = models.CharField(max_length=250)
    tipo_persona = models.CharField(max_length=100, choices=TIPO_PERSONA)
    cedula = models.CharField(max_length=13, unique=True, null=False, validators=[validate_cedula])
    tarjeta_credito = models.CharField(max_length=20, null=False, validators=[validate_cc])
    limite_credito = models.DecimalField(max_digits=7, decimal_places=2)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=250)
    cedula = models.CharField(max_length=13, unique=True, null=False, validators=[validate_cedula])
    tanda_labor = models.CharField(max_length=100, choices=TANDAS)
    porciento_comision = models.IntegerField(default = 0, 
    validators=[MaxValueValidator(100), MinValueValidator(0)])
    fecha_ingreso = models.DateField()
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre

class Inspeccion(models.Model):
    inspeccion_vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ralladuras = models.BooleanField()
    porcentaje_combustible = models.IntegerField(default = 0, 
    validators=[MaxValueValidator(100), MinValueValidator(0)])
    goma_repuesto = models.BooleanField()
    gato = models.BooleanField()
    roturas_cristal = models.BooleanField()
    goma_uno = models.BooleanField()
    goma_dos = models.BooleanField()
    goma_tres = models.BooleanField()
    goma_cuatro = models.BooleanField()
    inspeccion_fecha = models.DateField(auto_now_add=True)
    inspeccion_empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    estado = models.BooleanField()

    class Meta:
        verbose_name_plural = "Inspecciones"  

class Renta(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, limit_choices_to = {"estado" : True})
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_renta = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    monto_por_dia = models.DecimalField(max_digits=7, decimal_places=2)
    cantidad_dias = models.PositiveIntegerField()
    comentario = models.TextField()
    estado = models.BooleanField()

    def __str__(self):
        return str(self.fecha_renta) + self.vehiculo.descripcion


    def save(self, *args, **kwargs):
        if not self.fecha_devolucion:
            self.vehiculo.estado = False
        else:
            self.vehiculo.estado = True
        self.vehiculo.save()
        return super(Renta, self).save(*args, **kwargs)



# Create your models here.
