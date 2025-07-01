from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()  # ← usa o modelo definido em AUTH_USER_MODEL


class Habito(models.Model):
    FREQUENCIA_CHOICES = [
        ('D', 'Diário'),
        ('S', 'Semanal'),
        ('M', 'Mensal'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    frequencia = models.CharField(max_length=1, choices=FREQUENCIA_CHOICES)
    hora_sugerida = models.TimeField(null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habitos')

    def __str__(self):
        return self.nome


class RegistroHabito(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name='registros')
    data = models.DateField()
    feito = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)

    class Meta:
        unique_together = ('habito', 'data')  # Um registro por hábito por dia

    def __str__(self):
        return f"{self.habito.nome} - {self.data}"
