from django import forms 
from .models import Paquete

class PaqueteForm(forms.ModelForm):
    class Meta:
        model = Paquete
        fields = ('titulo', 'equipo', 'bolas', 'precio', 'descripcion', 'valido')
        widgets = {
        	'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Titulo'}),
        	'equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Equipo'}), 
        	'bolas': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Balas'}),
            'precio': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Precio'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'valido': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valides'}),
        }
        labels = {
        	'titulo':'', 'equipo':'', 'bolas':'', 'precio':'', 'descripcion':'', 'valido':''
        }