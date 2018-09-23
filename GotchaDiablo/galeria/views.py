from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Foto, Video
from .forms import FotoForm, VideoForm

# Create your views here.
class FotosListView(ListView):
    model = Foto
    template_name = 'galeria/foto_list.html'
    paginate_by = 9

class FotosDetailView(DetailView):
    model = Foto

@method_decorator(staff_member_required, name='dispatch')
class FotosAgrega(CreateView):
    model = Foto
    form_class = FotoForm
    success_url = reverse_lazy('fotos:fotos')

@method_decorator(staff_member_required, name='dispatch')
class FotosUpdate(UpdateView):
    model = Foto
    form_class = FotoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
    	return reverse_lazy('fotos:actualizar', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class FotosDelete(DeleteView):
    model = Foto
    success_url = reverse_lazy('fotos:fotos')




class VideosListView(ListView):
    model = Video
    template_name = 'galeria/video_list.html'
    paginate_by = 9

class VideosDetailView(DetailView):
    model = Video

@method_decorator(staff_member_required, name='dispatch')
class VideosAgrega(CreateView):
    model = Video
    form_class = VideoForm
    success_url = reverse_lazy('videos:videos')

@method_decorator(staff_member_required, name='dispatch')
class VideosUpdate(UpdateView):
    model = Video
    form_class = VideoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
    	return reverse_lazy('videos:actualizar', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class VideosDelete(DeleteView):
    model = Video
    success_url = reverse_lazy('videos:videos')
