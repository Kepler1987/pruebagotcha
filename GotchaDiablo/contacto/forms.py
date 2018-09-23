from django import forms

class Contactform(forms.Form):
	name = forms.CharField(label='Nombre', required=True, widget=forms.TextInput(
		attrs={'class':'form-control', 'placeholder':'Escribe tu Nombre'}
	), min_length=3, max_length=50)
	email = forms.EmailField(label='Correo', required=True, widget=forms.EmailInput(
		attrs={'class':'form-control', 'placeholder':'Escribe tu Correo'}
	), min_length=3, max_length=50)
	content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
		attrs={'class':'form-control', 'rows':5, 'placeholder':'Escribe tu Mensaje'}
	), min_length=20, max_length=200) 