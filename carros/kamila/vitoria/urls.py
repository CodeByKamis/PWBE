from django.urls import path
from . import views
# essas são as urls que você usa para acessar cada campo quando colocar o projeto para rodar
urlpatterns = [
    path('carros/', views.read_carros),#ele vai mostrar todos os carros
    path('carros/buscar/<int:pk>', views.pegar_carro),#você vai poder buscar um carro específico a partir do id dele
    path('carros/criar/', views.create_carro),#você vai poder criar um novo carro
    path('carros/atualizar/<int:pk>', views.update_carro),#você vai poder atualizar as informações do carro a partir do id dele
    path('carros/apagar/<int:pk>', views.delete_carro)#você vai poder apagar o carro a partir do id dele
]