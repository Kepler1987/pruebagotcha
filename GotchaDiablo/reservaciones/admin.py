from django.contrib import admin
from .models import Reservacion

# Register your models here.
class ReservacionAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	fields = ('user', 'nombre', 'pub_date', 'correo', 'telefono', 'paquete')


admin.site.register(Reservacion, ReservacionAdmin)