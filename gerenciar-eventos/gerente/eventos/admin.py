from django.contrib import admin
from .models import Postagem#importei a class postagens com suas funcionalidades
admin.site.register(Postagem)#puxei a class para registro para admin 
