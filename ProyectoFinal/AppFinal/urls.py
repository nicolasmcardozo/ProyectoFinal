from django.urls import path
from AppFinal import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('futbol', views.futbol,name="Futbol"),
    path('tenis', views.tenissingle,name="Tenis"),
    path('volley', views.volley,name="Volley"),
    path('busquedaEquipoFutbol', views.busquedaEquipoFutbol,name="busquedaEquipoFutbol"),
    path('buscarEquipoFutbol/', views.buscarEquipoFutbol),
    path('anotarseFutbol', views.anotarseFutbol,name="anotarseFutbol"),
    path('login',views.login_request,name='Login'),
    path('register',views.register,name='Register'),
    path('logout',LogoutView.as_view(template_name='AppFinal/logout.html'),name='Logout'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
]

