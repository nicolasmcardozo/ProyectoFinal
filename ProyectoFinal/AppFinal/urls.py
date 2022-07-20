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
    path('futbol/list',views.FutbolList.as_view(),name='List'),
    path(r'(?P<pk>\d+)$',views.FutbolDetalle.as_view(),name='Detail'),
    path(r'(?P<pk>\d+)$',views.FutbolDetalle1.as_view(),name='Detaill'),
    path(r'^nuevo$',views.FutbolCreacion.as_view(),name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.FutbolUpdate.as_view(),name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.FutbolDelete.as_view(),name='Delete'),
]

