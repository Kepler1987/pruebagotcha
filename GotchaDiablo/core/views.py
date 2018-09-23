from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render
from paquetes.models import Paquete


class InicioListView(ListView):
    model = Paquete
    template_name = "core/inicio.html"

class UbicacionPageView(TemplateView):
    template_name = "core/ubicacion.html"