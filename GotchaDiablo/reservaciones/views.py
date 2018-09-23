from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Reservacion 
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import ReservacionForm

# Create your views here.

class Reservaciones(CreateView):
	model = Reservacion
	form_class = ReservacionForm
	template_name = 'reservaciones/crear_reservacion.html'
	success_url = reverse_lazy('reservacion')
    
@method_decorator(staff_member_required, name='dispatch')
class ReservacionListView(ListView):

    model = Reservacion
    paginate_by = 20  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context