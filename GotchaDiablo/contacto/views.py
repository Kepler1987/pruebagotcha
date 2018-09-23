from django.shortcuts import render, redirect
from .forms import Contactform
from django.core.mail import EmailMessage
from django.urls import reverse

# Create your views here.
def contacto(request):
	contact_form = Contactform()
	if request.method == "POST":
		contact_form = Contactform(data=request.POST)
		if contact_form.is_valid():
			name = request.POST.get('name', '')
			email = request.POST.get('email', '')
			content = request.POST.get('content', '')
			#senviamos el correo y direccionamos
			email = EmailMessage(
				"Gotcha Diablo: Nuevo mensaje de contacto",
				"De: {} <{}> \n\nEscribio:\n\n{}".format(name, email, content),
				"no-contestar@inbox.mailtrap.io",
				["keplerreyes@gmail.com"],
				reply_to=[email]
			)
			try:
				email.send()
				return redirect(reverse('contacto')+"?ok")
			except Exception as e:
				return redirect(reverse('contacto')+"?fail")

	return render(request, "contacto/contacto.html",{'formulario':contact_form})