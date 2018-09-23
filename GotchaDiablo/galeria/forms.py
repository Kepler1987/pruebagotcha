from django import forms 
from .models import Foto, Video

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ('foto', 'titulo', 'descripcion')
        widgets = {
        	'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'titulo': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Titulo'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control mt-3'}),
        }
        labels = {
        	'foto':'', 'titulo':'', 'descripcion':''
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('video', 'titulo', 'descripcion')
        widgets = {
            'video': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'titulo': forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'Titulo'}), 
            'descripcion': forms.Textarea(attrs={'class':'form-control mt-3'}),
        }
        labels = {
            'video':'', 'titulo':'', 'descripcion':''
        }
