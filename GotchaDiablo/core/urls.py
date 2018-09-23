from django.urls import path
from .views import InicioListView, UbicacionPageView

urlpatterns = [
    path('', InicioListView.as_view(), name="inicio"),
    path('ubicacion/', UbicacionPageView.as_view(), name="ubicacion"),
]