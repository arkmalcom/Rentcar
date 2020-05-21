from django.contrib import admin
from rentcar.models import TipoVehiculo, Marca, Modelo, TipoCombustible, Vehiculo, Cliente, Empleado, Inspeccion, Renta
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.safestring import mark_safe

class TipoVehiculoResource(resources.ModelResource):
    class Meta:
        model = TipoVehiculo

class MarcaResource(resources.ModelResource):
    class Meta:
        model = Marca

class ModeloResource(resources.ModelResource):
    class Meta:
        model = Modelo

class TipoCombustibleResource(resources.ModelResource):
    class Meta:
        model = TipoCombustible

class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo

class ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class EmpleadoResource(resources.ModelResource):
    class Meta:
        model = Empleado

class InspeccionResource(resources.ModelResource):
    class Meta:
        model = Inspeccion

class RentaResource(resources.ModelResource):
    class Meta:
        model = Renta

class TipoVehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TipoVehiculoResource
    list_display = ('descripcion', 'estado')
    search_fields = ('descripcion', 'estado')

class MarcaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = MarcaResource
    list_display = ('descripcion', 'estado')
    search_fields = ('descripcion', 'estado')

class ModeloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ModeloResource
    list_display = ('descripcion', 'estado')
    search_fields = ('descripcion', 'estado')

class TipoCombustibleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = TipoCombustibleResource
    list_display = ('descripcion', 'estado')
    search_fields = ('descripcion', 'estado')

class VehiculoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = VehiculoResource
    list_display = ('descripcion', 'no_chasis', 'no_motor', 'no_placa', 'tipo_vehiculo', 'marca_vehiculo', 'modelo_vehiculo', 'combustible_vehiculo', 'estado', 'image_tag',)
    search_fields = ('descripcion', 'no_chasis', 'no_motor', 'no_placa', 'tipo_vehiculo__descripcion', 'marca_vehiculo__descripcion', 'modelo_vehiculo__descripcion', 'combustible_vehiculo__descripcion')

class ClienteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = ClienteResource
    list_display = ('nombre', 'tipo_persona', 'cedula', 'tarjeta_credito')
    search_fields = ('nombre', 'tipo_persona', 'cedula', 'tarjeta_credito')

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EmpleadoResource
    list_display = ('nombre', 'cedula', 'tanda_labor', 'porciento_comision', 'fecha_ingreso', 'estado')
    search_fields = ('nombre', 'cedula', 'tanda_labor', 'porciento_comision', 'fecha_ingreso')

class InspeccionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = InspeccionResource
    list_display = ('inspeccion_vehiculo', 'cliente', 'inspeccion_empleado', 'inspeccion_fecha')
    search_fields = ('inspeccion_vehiculo', 'cliente', 'inspeccion_empleado', 'inspeccion_fecha')

class RentaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RentaResource
    list_display = ('fecha_renta', 'cliente', 'vehiculo', 'empleado', 'monto_por_dia', 'cantidad_dias', 'fecha_devolucion', 'comentario', 'devolver_boton', 'get_imagen')
    search_fields = ('empleado__nombre', 'vehiculo__descripcion', 'cliente__nombre', 'comentario')

    def get_imagen(self, obj):
        return mark_safe('<img src="%s" style="width: 150px; height:150px;" />' % obj.vehiculo.imagen.url)
    get_imagen.short_description = 'Imagen'

    def devolver_boton(self, obj):
        if(not obj.fecha_devolucion and obj.vehiculo.estado == False):
           return format_html('<a class="button" href="%s/devolver/">Devolver</a>' % obj.id)
    devolver_boton.short_description = "Marcar devolucion"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<path:object_id>/devolver/', self.admin_site.admin_view(self.devolver))
        ]
        return custom_urls + urls

    def devolver(self, request, object_id, form_url=''):
        Renta.objects.filter(pk=object_id).update(fecha_devolucion=timezone.now())
        vehiculo_id = Renta.objects.get(pk=object_id).vehiculo.id
        Vehiculo.objects.filter(pk=vehiculo_id).update(estado=True)
        return HttpResponseRedirect('../../')
    
    def get_fields(self, request, obj=None):
        fields = super(RentaAdmin, self).get_fields(request, obj)
        for field in fields:
            if field == 'vehiculo' and obj is not None:
                continue
            if field == 'fecha_devolucion':
                continue
            yield field

# Register your models here.

admin.site.register(TipoVehiculo, TipoVehiculoAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Modelo, ModeloAdmin)
admin.site.register(TipoCombustible, TipoCombustibleAdmin)
admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Inspeccion, InspeccionAdmin)
admin.site.register(Renta, RentaAdmin)
