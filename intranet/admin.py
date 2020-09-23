from django.contrib import admin
from .models import Formulario
from easy_maps.widgets import AddressWithMapWidget
from django import forms

# Register your models here.

# admin.site.register(Formulario)

# Define the admin class
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('get_nombre_completo','telefono', 'pais')

    fieldsets = (
        ('Cliente', {
            'fields': ('nombre', 'apellido', 'telefono')
        }),
        ('Acceso', {
            'fields': ('permiso',)
        }),
        ('Direccion', {
            'fields': (('calle', 'numero'),'ciudad','pais')
        }),
         ('Mapa', {
            'fields': ('address',)
        }),  
    )
	
    def get_queryset(self, request):
        # Obtenemos el listado de todos los formularios exitentes 
        qs = super(FormularioAdmin, self).get_queryset(request)
        # Si es el request/solicitud lo realiza un superUser se retorna todo
        # Sino se filtra por los usuarios que tienen acceso.
        if request.user.is_superuser:
            return qs
        else:
        	return qs.filter(permiso__id = request.user.id)

    def get_readonly_fields(self, request, obj=None):
	    user = request.user
	    if user.has_perm('Formulario.asignar'):
	        return []
	    else:
	        return ['permiso']    	

    class FormularioForm(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }
    form = FormularioForm

    def response_change(self, request, obj):
    	obj.address = ""
    	if( obj.numero is None): obj.address = obj.calle + ", " + obj.ciudad + ", " + obj.pais
    	else : obj.address = obj.calle + ", " + obj.numero + ", " + obj.ciudad + ", " + obj.pais
    	obj.save()
    	return super().response_change(request, obj)

    def response_add(self, request, obj, post_url_continue=None):
    	obj.address = ""
    	if( obj.numero is None): obj.address = obj.calle + ", " + obj.ciudad + ", " + obj.pais
    	else : obj.address = obj.calle + ", " + obj.numero + ", " + obj.ciudad + ", " + obj.pais
    	obj.save()
    	return super().response_add(request, obj)	

# Register the admin class with the associated model
admin.site.register(Formulario, FormularioAdmin)