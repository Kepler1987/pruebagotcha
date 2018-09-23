from django.db import models

# Create your models here.
class Paquete(models.Model):
	
	titulo = models.CharField(verbose_name='Titulo', max_length=100)
	equipo = models.CharField(verbose_name='Equipo', max_length=250)
	bolas = models.IntegerField(verbose_name='Balas')
	precio = models.IntegerField(verbose_name='Precio')
	descripcion = models.TextField(verbose_name='Descripcion')
	valido = models.CharField(verbose_name='Valides', max_length=100)
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)


	class Meta:
		verbose_name='paquete'
		verbose_name_plural='paquetes'
		ordering=['created']

	def __str__(self):
		return self.titulo
			