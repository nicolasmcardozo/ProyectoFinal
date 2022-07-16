from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.forms import FutbolFormulario,TenisFormulario,VolleyFormulario
from AppFinal.models import Futbol, TenisSingle, Volley
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin



def inicio(request):
	return render(request,"AppFinal/inicio.html")


def futbol(request):
	if request.method == 'POST':

		miFormulario = FutbolFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data
			futbol = Futbol(nombre_equipo = informacion['nombre_equipo'], integrantes = informacion['integrantes'],email_representante = informacion['email_representante'],telefono_contacto = informacion['telefono_contacto'],id_torneo = informacion['id_torneo'])
			futbol.save()
			return render(request,"AppFinal/inicio.html")

	else:
		miFormulario = FutbolFormulario()

	return render(request,"AppFinal/futbol.html",{"miFormulario":miFormulario})


def tenissingle(request):

	if request.method == "POST":

		miFormulario = TenisFormulario(request.POST)

		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data

			tenissingle = TenisSingle(nombre_participante=informacion["nombre_participante"],email_tenista = informacion["email_tenista"], telefono_contacto = informacion["telefono_contacto"] ,id_torneo=informacion["id_torneo"])

			tenissingle.save()

			return render(request,"AppFinal/inicio.html")

	else:
		miFormulario = TenisFormulario()
	
	return render(request,"AppFinal/tenis.html",{"miFormulario":miFormulario})

def volley(request):

	if request.method == "POST":

		miFormulario = VolleyFormulario(request.POST)

		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data

			volley = Volley(nombre_equipo=informacion["nombre_equipo"],integrantes = informacion["integrantes"], email_representante = informacion["email_representante"],telefono_contacto = informacion["telefono_contacto"],id_torneo = informacion["id_torneo"])

			volley.save()

			return render(request,"AppFinal/inicio.html")

	else:
		miFormulario = VolleyFormulario()
	
	return render(request,"AppFinal/volley.html",{"miFormulario":miFormulario})
