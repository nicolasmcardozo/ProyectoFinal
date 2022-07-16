from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.forms import CursoFormulario,ProfesorFormulario, EstudianteFormulario, EntregableFormulario, UserRegisterForm, UserEditForm
from AppCoder.models import Futbol, TenisSingle, Volley
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def inicio(request):
	return render(request,"AppCoder/inicio.html")

@login_required
def futbol(request):
	if request.method == 'POST':

		miFormulario = Futbol(request.POST)
		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data
			curso = Curso (nombre = informacion['nombre'], camada = informacion['camada'])
			curso.save()
			return render(request,"AppCoder/inicio.html")

	else:
		miFormulario = CursoFormulario()

	return render(request,"AppCoder/cursos.html",{"miFormulario":miFormulario})

@login_required
def profesores(request):

	if request.method == "POST":

		miFormulario = ProfesorFormulario(request.POST)

		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data

			profesor = Profesor (nombre=informacion["nombre"],apellido = informacion["apellido"], emails = informacion["emails"] ,profesion=informacion["profesion"])

			profesor.save()

			return render(request,"AppCoder/inicio.html")

	else:
		miFormulario = ProfesorFormulario()
	
	return render(request,"AppCoder/profesores.html",{"miFormulario":miFormulario})


def busquedaCamada(request):

	return render(request,"AppCoder/busquedaCamada.html")


def buscar(request):

    if  request.GET["camada"]:

            #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
            camada = request.GET['camada'] 
            cursos = Curso.objects.filter(camada__icontains=camada)

            return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})

    else: 

            respuesta = "No enviaste datos"

                    #No olvidar from django.http import HttpResponse
                    #return HttpResponse(respuesta)
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})

def leerCursos(request):

	cursos = Curso.objects.all() 

	contexto={"cursos":cursos}

	return render(request, "AppCoder/leerCursos.html",contexto)

def eliminarCursos(request, curso_nombre):

	cursos = Curso.objects.get(nombre=curso_nombre)
	cursos.delete()

	cursos = Curso.objects.all()
    
	contexto = {"cursos":cursos}

	return render(request,"AppCoder/leerCursos.html",contexto)

def editarCurso(request, curso_nombre):

	cursos = Curso.objects.get(nombre=curso_nombre)

	if request.method == 'POST':
		miFormulario = CursoFormulario(request.POST)
		print(miFormulario)
		if miFormulario.is_valid:
			informacion = miFormulario.cleaned_data

			cursos.nombre = informacion['nombre']
			cursos.camada = informacion['camada']

			cursos.save()

			return render(request,"AppCoder/inicio.html")
	else:
		miFormulario = CursoFormulario(initial={'nombre':cursos.nombre, 'camada':cursos.camada})

	return render(request,"AppCoder/editarCurso.html",{"miFormulario":miFormulario,"curso_nombre":curso_nombre})


def estudiantes(request):

	if request.method == "POST":

		miFormulario = EstudianteFormulario(request.POST)

		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data

			estudiante = Estudiante (nombre=informacion["nombre"],apellido = informacion["apellido"], emails = informacion["emails"])

			estudiante.save()

			return render(request,"AppCoder/inicio.html")

	else:
		miFormulario = EstudianteFormulario()
	
	return render(request,"AppCoder/estudiantes.html",{"miFormulario":miFormulario})

def entregables(request):

	if request.method == "POST":

		miFormulario = EntregableFormulario(request.POST)

		print(miFormulario)

		if miFormulario.is_valid:

			informacion = miFormulario.cleaned_data

			entregables = Entregable (nombre=informacion["nombre"],fechaDeEntrega = informacion["fechaDeEntrega"], entregado = informacion["entregado"])

			entregables.save()

			return render(request,"AppCoder/inicio.html")

	else:
		miFormulario = EntregableFormulario()
	
	return render(request,"AppCoder/entregables.html",{"miFormulario":miFormulario})


class ProfesorList(LoginRequiredMixin, ListView):
	
	model = Profesor
	template_name = "AppCoder/profesores_list.html"

class ProfesorDetalle(DetailView):

	model = Profesor
	template_name = "AppCoder/profesor_detalle.html"

class ProfesorCreacion(CreateView):

	model = Profesor
	success_url = "/AppCoder/profesor/list"
	fields= ['nombre','apellido','emails','profesion']


class ProfesorDelete(DeleteView):

	model = Profesor
	success_url = "/AppCoder/profesor/list"

class ProfesorUpdate(UpdateView):

    model = Profesor
    success_url = "/AppCoder/profesor/list"
    fields= ['nombre','apellido','emails','profesion']

def login_request(request):


      if request.method == "POST":
            form = AuthenticationForm(request, data = request.POST)

            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')

                  user = authenticate(username=usuario, password=contra)

            
                  if user is not None:
                        login(request, user)
                       
                        return render(request,"AppCoder/inicio.html",{"mensaje":f"Bienvenido {usuario}"} )
                  else:
                        
                        return render(request,"AppCoder/inicio.html",{"mensaje":"Error, datos incorrectos"} )

            else:
                        
                        return render(request,"AppCoder/inicio.html",{"mensaje":"Error, formulario erroneo"})

      form = AuthenticationForm()

      return render(request,"AppCoder/login.html", {'form':form} )

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			form.save()
			return render(request, "AppCoder/inicio.html",{"mensaje":"Usuario Creado"})
	else:
		form = UserRegisterForm()
	return render(request,"AppCoder/registro.html",{"form":form})

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

                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      #En caso que no sea post
      else: 
            #Creo el formulario con los datos que voy a modificar
            miFormulario= UserEditForm(initial={ 'email':usuario.email}) 

      #Voy al html que me permite editar
      return render(request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
