from django.contrib import admin
from .models import Paquete

# Register your models here.
class PaqueteAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')


admin.site.register(Paquete, PaqueteAdmin)