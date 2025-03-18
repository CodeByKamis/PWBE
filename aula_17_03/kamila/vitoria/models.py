from django.db import models

class Carro(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    qntRodas = models.PositiveIntegerField()
    ano = models.PositiveIntegerField()
    cor = models.CharField(max_length=255)
    escolhas_combustivel = (
        ('GASOLINA', 'Gasolina'),
        ('ETANOL', 'Etanol'),
        ('GNV', 'gnv'),
        ('ELETRICO', 'Eletrico'),
        ('ALCOOL', 'Alcool'),
        ('DIESEL', 'Diesel'),
        ('FB', 'feedback'),
        )
    combustivel = models.CharField(max_length=9, choices=escolhas_combustivel)
    def __str__(self):
        return self.nome
