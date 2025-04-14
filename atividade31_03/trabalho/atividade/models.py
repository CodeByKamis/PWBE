from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioDS16(AbstractUser):
    idade = models.PositiveIntegerField()
    telefone = models.CharField(max_length=255, null=True, blank=True)
    biografia = models.CharField(max_length=255, null=True, blank=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    escolaridade = models.CharField(max_length=255, null=True, blank=True)
    animais = models.PositiveIntegerField(null=True, blank=True)

    REQUIRED_FIELDS= ['idade', 'telefone']#quando é um campo obrigatorio você tem que fazer isso
    
    def __str__(self):
        return self.username