from django.http import HttpResponse
from django.shortcuts import render
from AppFinal.forms import FutbolFormulario,TenisFormulario,VolleyFormulario,UserRegisterForm,UserEditForm
from AppFinal.models import Futbol, TenisSingle, Volley
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



def inicio(request):
	return render(request,'AppFinal/inicio.html', {})


def futbol(request): #CORREGIDO
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

@login_required
def anotarseFutbol(request): #CORREGIDO
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

	return render(request,"AppFinal/anotarseFutbol.html",{"miFormulario":miFormulario})


def tenissingle(request):

	if request.method == "POST":

		miFormulario = TenisFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid:
			informacion = miFormulario.cleaned_data
			tenissingle = TenisSingle (nombre_participante=informacion["nombre_participante"],email_tenista = informacion["email_tenista"], telefono_contacto = informacion["telefono_contacto"] ,id_torneo=informacion["id_torneo"])
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

@login_required
def busquedaEquipoFutbol(request):
	return render(request,"AppFinal/busquedaEquipoFutbol.html")

def buscarEquipoFutbol(request):
	if request.GET["nombre_equipo"]:
		nombre_equipo = request.GET['nombre_equipo'] 
		equipos_futbol = Futbol.objects.filter(nombre_equipo__icontains=nombre_equipo)
		return render(request, "AppFinal/resultadosBusquedaFutbol.html", {"equipos_futbol":equipos_futbol, "nombre_equipo":nombre_equipo})

	else:
		respuesta = "No enviaste datos"
	return render(request,"AppFinal/inicio.html",{"respuesta":respuesta})

def login_request(request): #REVISAR

      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppFinal/inicio.html",{"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppFinal/inicio.html",{"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppFinal/inicio.html",{"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppFinal/login.html", {'form':form} )

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			form.save()
		return render(request, "AppFinal/inicio.html",{"mensaje":"Usuario Creado"})
	else:
		form = UserRegisterForm()
		return render(request,"AppFinal/registro.html",{"form":form})

@login_required
def editarPerfil(request):

      #Instancia del login
      usuario = request.user
     
      #Si es metodo POST hago lo mismo que el agregar
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            if miFormulario.is_valid():   #Si pasó la validación de Django

            	informacion = miFormulario.cleaned_data
            
                  #Datos que se modificarán
            	usuario.email = informacion['email']
            	usuario.password1 = informacion['password1']
            	usuario.password2 = informacion['password2']
            	usuario.first_name = informacion['first_name']
            	usuario.last_name = informacion['last_name']
            	usuario.save()

            return render(request, "AppFinal/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email,'first_name':usuario.first_name,'last_name':usuario.last_name}) 

      #Voy al html que me permite editar
      return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})

class FutbolList(LoginRequiredMixin, ListView):
	model = Futbol
	template_name = "AppFinal/futbol_list.html"

class FutbolDetalle(LoginRequiredMixin, DetailView):
	model = Futbol
	template_name = "AppFinal/futbol_detalle.html"

class FutbolDetalle1(LoginRequiredMixin, DetailView):
	model = Futbol
	template_name = "AppFinal/futbol_detalle1.html"

class FutbolCreacion(LoginRequiredMixin, CreateView):

	model = Futbol
	success_url = "/AppFinal/futbol"
	fields= ['nombre_equipo','integrantes','email_representante','telefono_contacto','id_torneo']


class FutbolDelete(LoginRequiredMixin, DeleteView):

	model = Futbol
	success_url = "/AppFinal/futbol"

class FutbolUpdate(LoginRequiredMixin, UpdateView):

    model = Futbol
    success_url = "/AppFinal/futbol"
    fields= ['nombre_equipo','integrantes','email_representante','telefono_contacto','id_torneo']

###VIEW###

@login_required
def anotarseVolley(request):
	if request.method == 'POST':

		miFormulario = VolleyFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data
			volley = Volley(nombre_equipo = informacion['nombre_equipo'], integrantes = informacion['integrantes'],email_representante = informacion['email_representante'],telefono_contacto = informacion['telefono_contacto'],id_torneo = informacion['id_torneo'])
			volley.save()
			return render(request,"AppFinal/inicio.html")

	else:
		miFormulario = VolleyFormulario()

	return render(request,"AppFinal/anotarseVolley.html",{"miFormulario":miFormulario})

@login_required
def anotarseTenis(request):
	if request.method == 'POST':

		miFormulario = TenisFormulario(request.POST)
		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data
			tenis = TenisSingle(nombre_participante = informacion['nombre_participante'], email_tenista = informacion['email_tenista'], telefono_contacto = informacion['telefono_contacto'],id_torneo = informacion['id_torneo'])
			tenis.save()
		return render(request,"AppFinal/inicio.html")

	else:
		miFormulario = TenisFormulario()

	return render(request,"AppFinal/anotarseTenis.html",{"miFormulario":miFormulario})


@login_required
def busquedaEquipoVolley(request):
	return render(request,"AppFinal/busquedaEquipoVolley.html")

def buscarEquipoVolley(request):
	if request.GET["nombre_equipo"]:
		nombre_equipo = request.GET['nombre_equipo'] 
		equipos_volley = Volley.objects.filter(nombre_equipo__icontains=nombre_equipo)
		return render(request, "AppFinal/resultadosBusquedaVolley.html", {"equipos_volley":equipos_volley, "nombre_equipo":nombre_equipo})

	else:

		respuesta = "No enviaste datos"

	return render(request,"AppFinal/inicio.html",{"respuesta":respuesta})

@login_required
def busquedaEquipoTenis(request):
	return render(request,"AppFinal/busquedaEquipoTenis.html")

def buscarEquipoTenis(request):
	if request.GET["nombre_participante"]:
		nombre_participante = request.GET['nombre_participante'] 
		equipos_tenis = TenisSingle.objects.filter(nombre_participante__icontains=nombre_participante)
		return render(request, "AppFinal/resultadosBusquedaTenis.html", {"equipos_tenis":equipos_tenis, "nombre_participante":nombre_participante})

	else:

		respuesta = "No enviaste datos"

	return render(request,"AppFinal/inicio.html",{"respuesta":respuesta})

class VolleyList(LoginRequiredMixin, ListView):
	model = Volley
	template_name = "AppFinal/volley_list.html"

class VolleyDetalle(LoginRequiredMixin, DetailView):
	model = Volley
	template_name = "AppFinal/volley_detalle.html"

class VolleyCreacion(LoginRequiredMixin, CreateView):

	model = Volley
	success_url = "/AppFinal/volley"
	fields= ['nombre_equipo','integrantes','email_representante','telefono_contacto','id_torneo']


class VolleyDelete(LoginRequiredMixin, DeleteView):

	model = Volley
	success_url = "/AppFinal/volley"

class VolleyUpdate(LoginRequiredMixin, UpdateView):

    model = Volley
    success_url = "/AppFinal/volley"
    fields= ['nombre_equipo','integrantes','email_representante','telefono_contacto','id_torneo']

class TenisList(LoginRequiredMixin, ListView):
	model = TenisSingle
	template_name = "AppFinal/tenis_list.html"

class TenisDetalle(LoginRequiredMixin, DetailView):
	model = TenisSingle
	template_name = "AppFinal/tenis_detalle.html"

class TenisCreacion(LoginRequiredMixin, CreateView):

	model = TenisSingle
	success_url = "/AppFinal/tenis"
	fields= ['nombre_participante','email_tenista','telefono_contacto','id_torneo']


class TenisDelete(LoginRequiredMixin, DeleteView):

	model = TenisSingle
	success_url = "/AppFinal/tenis"

class TenisUpdate(LoginRequiredMixin, UpdateView):

    model = TenisSingle
    success_url = "/AppFinal/tenis"
    fields= ['nombre_participante','email_tenista','telefono_contacto','id_torneo']

def about(request):
	return render(request,"AppFinal/about.html")

