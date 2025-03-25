from django.db import models
#essa é a classe Postagem, que serão todas as informações para adicionar nos meus posts
class Postagem(models.Model):
    nome = models.CharField(max_length=255)#esse texto tem limite de 255 caracteres
    descricao = models.TextField()#é um texto grande, então não tem limite
    date_time = models.DateTimeField(auto_now_add=True)
    local =  models.CharField(max_length=255)
    escolha_categoria = (#esse é uma lista de opções
        ('Culto', 'CULTO'),
        ('Aniversario', 'ANIVERSARIO'),
        ('Churrasco', 'CHURRASCO'),
    )
    categoria = models.CharField(max_length=255, choices=escolha_categoria)
    def __str__(self):
        return self.nome
# Create your models here.
