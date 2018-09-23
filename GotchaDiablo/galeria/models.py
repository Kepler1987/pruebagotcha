from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_upload_to(instance, filename):
	old_instance = Foto.objects.get(pk=instance.pk)
	old_instance.foto.delete()
	return 'fotos/'+ filename

def customv_upload_to(instance, filename):
	old_instance = Video.objects.get(pk=instance.pk)
	old_instance.video.delete()
	return 'videos/'+ filename

# Create your models here.
class Foto(models.Model):
	foto = models.ImageField(upload_to='fotos', verbose_name='Foto', null=True, blank=True)
	titulo = models.CharField(verbose_name='Titulo', max_length=100, null=True, blank=True)
	descripcion = models.TextField(verbose_name='Descripcion', null=True, blank=True)
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)

	class Meta:
		verbose_name='foto'
		verbose_name_plural='fotos'
		ordering=['created']

	def __str__(self):
		return self.titulo

class Video(models.Model):
	video = models.FileField(verbose_name='Video', upload_to='videos', null=True, blank=True)
	titulo = models.CharField(verbose_name='Titulo', max_length=100, null=True, blank=True)
	descripcion = models.TextField(verbose_name='Descripcion', null=True, blank=True)
	created = models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
	updated = models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)

	class Meta:
		verbose_name='video'
		verbose_name_plural='videos'
		ordering=['created']

	def __str__(self):
		return self.titulo
