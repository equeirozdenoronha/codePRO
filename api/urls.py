# api/urls.py
from django.urls import include, path

urlpatterns = [
    path('users/', include('usuarios.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]