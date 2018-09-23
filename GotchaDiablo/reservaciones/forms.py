from django import forms 
from .models import Reservacion

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ('nombre', 'pub_date', 'correo', 'telefono', 'paquete')
        widgets = {
        	'nombre': forms.TextInput(attrs={'class':'form-control mb-5', 'placeholder':'Nombre'}),
        	'pub_date': forms.DateInput(attrs={'class':'form-control mb-5', 'placeholder':'Fecha de reservación'}),
        	'correo': forms.EmailInput(attrs={'class':'form-control mb-5', 'placeholder':'Correo'}), 
        	'telefono': forms.NumberInput(attrs={'class':'form-control mb-5', 'placeholder':'Telefono'}),
            'paquete': forms.Select(attrs={'class':'form-control mb-5', 'placeholder':'Paquete'}),
        }
        labels = {
        	'nombre':'','pub_date':'', 'correo':'', 'telefono':'', 'paquete':''
        }