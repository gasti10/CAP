from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User


# Create your models here.
class Formulario(models.Model):
    """
    Modelo que representa un formulario.
    """
    id = models.AutoField('Cliente',primary_key=True)

    nombre = models.CharField('Nombre', max_length=200, help_text="Ingrese el nombre del cliente", null=False)

    apellido = models.CharField('Apellido', max_length=200, help_text="Ingrese el apellido del cliente", null=False)

    telefono = models.CharField('Telefono', max_length=200, help_text="Ingrese el numero de telefono")

    calle = models.CharField('Calle', default="Tressens", max_length=200)

    ciudad = models.CharField('Ciudad', default="Calderón", max_length=200)

    numero = models.CharField('Numero', max_length=200, null=True, blank=True)

    pais = models.CharField('Pais', default="Argentina", max_length=200)

    """
    Relacion para saber que usuarios podrán visualizar el formulario
    """
    permiso = models.ManyToManyField( User, blank=True)    

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo, será lo que se vea en el admin
        """
        return "Cliente Nro = " + str(self.id) + " - " + self.nombre+ " " +self.apellido

    def get_absolute_url(self):
	    """
	    Devuelve el URL a una instancia particular de Formulario
	    """
	    return reverse('Formulario-detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Formularios"
        ordering = ["-id"]
        #Posible solución a las asignaciones sin filtro.
        permissions = (("asignar", "Asignar usuarios con acceso"),) 

    def get_nombre_completo(self):
        """
        Crea un string con el nombre y apellido
        """
        return self.apellido+ ", " +self.nombre
    get_nombre_completo.short_description = 'Nombre'     

    #Register the function to the property method
    def make_address(self):
        return  self.calle + ", " + self.numero + ", " + self.ciudad + ", " + self.pais
    
    """
    Atributo para que el mapa lea la dirección completa.
    """
    address = models.CharField('Dirección(se autocompleta)',max_length=200,default="Tressens, Calderón, Argentina",help_text="Se autocompleta con los datos ingresados arriba")