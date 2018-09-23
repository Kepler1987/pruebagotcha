from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Paquete
from .forms import PaqueteForm



# Create your views here.
class PaqueteListView(ListView):
    model = Paquete

class PaqueteDetailView(DetailView):
	model = Paquete

@method_decorator(staff_member_required, name='dispatch')
class PaqueteCreate(CreateView):
    model = Paquete
    form_class = PaqueteForm
    success_url = reverse_lazy('paquetes:paquetes')

@method_decorator(staff_member_required, name='dispatch')
class PaqueteUpdate(UpdateView):
    model = Paquete
    form_class = PaqueteForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
    	return reverse_lazy('paquetes:actualizar', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PaqueteDelete(DeleteView):
    model = Paquete
    success_url = reverse_lazy('paquetes:paquetes')