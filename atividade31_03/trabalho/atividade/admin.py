from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UsuarioDS16

class UsuarioDS16Admin(UserAdmin):
    list_display = ('username', 'password', 'biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')#lista o usuario

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('biografia', 'idade', 'telefone', 'endereco', 'escolaridade', 'animais')}),
    )#quando clicar em usuario específico vai aparecer isso do usuario


    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('idade', 'biografia', 'telefone')}),
    )#aqui ele mostra os campos quando a gente clica em criar um usuario

admin.site.register(UsuarioDS16, UsuarioDS16Admin)
