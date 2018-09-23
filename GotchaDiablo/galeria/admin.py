from django.contrib import admin
from .models import Foto, Video

# Register your models here.
class FotoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')


admin.site.register(Foto, FotoAdmin)

class VideoAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')


admin.site.register(Video, VideoAdmin)