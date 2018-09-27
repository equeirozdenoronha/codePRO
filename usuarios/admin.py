from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UsuarioForm, UsuarioChangeForm
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    add_form = UsuarioForm
    form = UsuarioChangeForm
    model = Usuario
    list_display = ['email', 'username', 'nome']
    search_fields = ('nome', 'email')
    list_filter = ('nome', 'email')
    list_per_page = 30

admin.site.register(Usuario, CustomUserAdmin)