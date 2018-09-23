from django.urls import path
from .views import FotosListView, FotosDetailView, FotosAgrega, FotosUpdate, FotosDelete, VideosListView, VideosDetailView, VideosAgrega, VideosUpdate, VideosDelete

fotos_patterns = ([
	path('', FotosListView.as_view(), name='fotos'),
	path('<int:pk>/<slug:slug>/', FotosDetailView.as_view(), name='foto'),
    path('agrega/', FotosAgrega.as_view(), name='agrega'),
    path('actualizar/<int:pk>/', FotosUpdate.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', FotosDelete.as_view(), name='eliminar'),
], 'fotos')

videos_patterns = ([
	path('', VideosListView.as_view(), name='videos'),
	path('<int:pk>/<slug:slug>/', VideosDetailView.as_view(), name='video'),
    path('agrega/', VideosAgrega.as_view(), name='agrega'),
    path('actualizar/<int:pk>/', VideosUpdate.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', VideosDelete.as_view(), name='eliminar'),
], 'videos')