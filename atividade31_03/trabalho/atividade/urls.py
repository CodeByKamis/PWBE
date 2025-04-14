from django.urls import path
from . import views

urlpatterns =[
    path('criar/', view=views.criar_usuario, name='criar_usuario'),
    path('logar/', view=views.logar_usuario, name='logar_usuario'),
    path('ver_usuario/', view=views.ver_usuario, name='ver_usuario'),
    path('read/', view=views.read, name='read'),
    path('update_usuario/<int:pk>/', view=views.update_usuario, name='update_usuario'),
    path('delete_usuario/<int:pk>/', view=views.delete_usuario, name='delete_usuario'),

]