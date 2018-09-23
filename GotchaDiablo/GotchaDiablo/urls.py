"""GotchaDiablo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from paquetes.urls import paquetes_patterns
from reservaciones.urls import reservacion_patterns
from galeria.urls import fotos_patterns, videos_patterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    #Path Nucleo
    path('', include('core.urls')),
	#Path Contacto
    path('contacto/', include('contacto.urls')),
    #Path Paquetes
    path('paquetes/', include(paquetes_patterns)),
    #Path Paquetes
    path('reservacion/', include(reservacion_patterns)),
    #Path Galeria
    path('galeria/fotos/', include(fotos_patterns)),
    path('galeria/videos/', include(videos_patterns)),
    # Path de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]
if settings.DEBUG:
	from django.conf.urls.static import static
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
