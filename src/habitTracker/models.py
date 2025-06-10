from django.db import models

from django.contrib.auth.models import User

class Rotina(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rotinas')

    def __str__(self):
        return self.nome
