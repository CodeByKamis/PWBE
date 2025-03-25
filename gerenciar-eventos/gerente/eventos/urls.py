from django.urls import path
from . import views

urlpatterns =[#essas são as urls que criei para rodar cada metodo do views
    path('eventos/', views.read_eventos ),
    path('eventos/buscar/<int:pk>', views.pegar_evento ),
    path('eventos/criar/', views.create_evento ),
    path('eventos/atualizar/<int:pk>', views.update_evento ),
    path('eventos/apagar/<int:pk>', views.delete_evento ),
]