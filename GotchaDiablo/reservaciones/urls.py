from django.urls import path
from .views import Reservaciones, ReservacionListView

reservacion_patterns = [
    path('', Reservaciones.as_view(), name="reservacion"),
    path('reservaciones/', ReservacionListView.as_view(), name="reservaciones"),
]