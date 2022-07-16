from django.contrib import admin

from  .models import * #importamos el archivo models


#registramos los modelos

admin.site.register(Futbol)

admin.site.register(Volley)

admin.site.register(TenisSingle)
