from django.urls import path, re_path
from AppFinal import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name= 'Inicio'),
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
    re_path(r'(?P<pk>\d+)$',views.FutbolDetalle.as_view(),name='Detail'),
    re_path(r'(?P<pk>\d+)$',views.FutbolDetalle1.as_view(),name='Detaill'),
    re_path(r'^nuevo$',views.FutbolCreacion.as_view(),name='New'),
    re_path(r'^editar/(?P<pk>\d+)$',views.FutbolUpdate.as_view(),name='Edit'),
    re_path(r'^borrar/(?P<pk>\d+)$',views.FutbolDelete.as_view(),name='Delete'),
    path('busquedaEquipoTenis', views.busquedaEquipoTenis,name="busquedaEquipoTenis"),
    path('buscarEquipoTenis/', views.buscarEquipoTenis),
    path('anotarseTenis', views.anotarseTenis,name="anotarseTenis"),
    path('busquedaEquipoVolley', views.busquedaEquipoVolley,name="busquedaEquipoVolley"),
    path('buscarEquipoVolley/', views.buscarEquipoVolley),
    path('anotarseVolley', views.anotarseVolley,name="anotarseVolley"),
    path('tenis/list',views.TenisList.as_view(),name='List1'),
    re_path(r'(?P<pk>\d+1)$',views.TenisDetalle.as_view(),name='Detail1'),
    re_path(r'^nuevo$',views.TenisCreacion.as_view(),name='New1'),
    re_path(r'^editar/(?P<pk>\d+1)$',views.TenisUpdate.as_view(),name='Edit1'),
    re_path(r'^borrar/(?P<pk>\d+1)$',views.TenisDelete.as_view(),name='Delete1'),
    path('volley/list',views.VolleyList.as_view(),name='List2'),
    re_path(r'(?P<pk>\d+2)$',views.VolleyDetalle.as_view(),name='Detail2'),
    re_path(r'^nuevo$',views.VolleyCreacion.as_view(),name='New2'),
    re_path(r'^editar/(?P<pk>\d+2)$',views.VolleyUpdate.as_view(),name='Edit2'),
    re_path(r'^borrar/(?P<pk>\d+2)$',views.VolleyDelete.as_view(),name='Delete2'),
    path('about',views.about,name='About'),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
]

