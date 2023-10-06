from django.contrib import admin
from django.urls import path, include  # Importa 'include' para incluir las URL de la API

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    
]   