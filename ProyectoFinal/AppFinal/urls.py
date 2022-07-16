from django.urls import path
from AppFinal import views 
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio,name="Inicio"),
    path('futbol', views.futbol,name="Futbol"),
    path('tenissingle', views.tenissingle,name="Tenis Single"),
    path('volley', views.volley,name="Volley"),
]

#asd