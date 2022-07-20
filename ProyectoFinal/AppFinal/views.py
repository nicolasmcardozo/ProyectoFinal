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

@login_required
def anotarseFutbol(request):
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

def login_request(request):


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
                  usuario.save()

                  return render(request, "AppFinal/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppFinal/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})