from django.db import models
from django.contrib.auth.models import User
from paquetes.models import Paquete

# Create your models here.
class Reservacion(models.Model):

	user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	nombre = models.CharField(verbose_name='Nombre', max_length=250) 
	pub_date = models.DateField(verbose_name='Fecha de Reservación') 
	correo = models.EmailField(verbose_name='Correo')
	telefono = models.IntegerField(verbose_name='Telefono')
	paquete = models.ForeignKey(Paquete, blank=True, null=True, on_delete=models.CASCADE)
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)

	class Meta:
		verbose_name='reservacion'
		verbose_name_plural='reservaciones'
		ordering=['created']

	def __str__(self):
		return self.correo

