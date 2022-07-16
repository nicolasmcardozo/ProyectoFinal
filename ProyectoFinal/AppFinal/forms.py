from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FutbolFormulario(forms.Form):

    nombre_equipo = forms.CharField(max_length=40)
    integrantes = forms.IntegerField()
    email_representante = forms.EmailField()
    telefono_contacto = forms.CharField(max_length=40)
    id_torneo = forms.IntegerField()

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



