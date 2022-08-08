from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FutbolFormulario(forms.Form):

    nombre_equipo = forms.CharField(max_length=40)
    integrantes = forms.IntegerField()
    email_representante = forms.EmailField()
    telefono_contacto = forms.CharField(max_length=40)
    id_torneo = forms.IntegerField()
    fecha_de_registro = forms.DateField()

class TenisFormulario(forms.Form):

    nombre_participante = forms.CharField(max_length=40)
    email_tenista = forms.EmailField()
    telefono_contacto = forms.CharField(max_length=40)
    id_torneo = forms.IntegerField()

class VolleyFormulario(forms.Form):

    nombre_equipo = forms.CharField(max_length=40)
    integrantes = forms.IntegerField()
    email_representante = forms.EmailField()
    telefono_contacto = forms.CharField(max_length=40)
    id_torneo = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contraseña',widget=forms.PasswordInput)
    last_name=forms.CharField()
    first_name = forms.CharField()


    class Meta:
        model = User
        fields=['username','email','password1','password2','last_name','first_name']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2','last_name','first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}


class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField(required=True)
