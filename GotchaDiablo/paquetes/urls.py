from django.urls import path
from .views import PaqueteListView, PaqueteDetailView, PaqueteCreate, PaqueteUpdate, PaqueteDelete

paquetes_patterns = ([
	path('', PaqueteListView.as_view(), name='paquetes'),
	path('<int:pk>/<slug:slug>/', PaqueteDetailView.as_view(), name='paquete'),
    path('crear/', PaqueteCreate.as_view(), name='crear'),
    path('actualizar/<int:pk>/', PaqueteUpdate.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', PaqueteDelete.as_view(), name='eliminar'),
], 'paquetes')