from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import date

User = get_user_model()  # usa o modelo definido em AUTH_USER_MODEL

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
    dias_semana = models.JSONField(default=list)  # armazenamos os dias
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habitos')

    def __str__(self):
        return self.nome

    def clean(self):
        # Validação para impedir nomes duplicados por usuário (case insensitive)
        if Habito.objects.filter(usuario=self.usuario, nome__iexact=self.nome).exclude(pk=self.pk).exists():
            raise ValidationError('Você já possui um hábito com esse nome.')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['usuario', 'nome'], name='unique_habito_por_usuario')
        ]


class RegistroHabito(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE, related_name='registros')
    data = models.DateField(default=date.today)
    feito = models.BooleanField(default=False)
    observacoes = models.TextField(blank=True)

    class Meta:
        unique_together = ('habito', 'data')  # Um registro por hábito por dia

    def __str__(self):
        return f"{self.habito.nome} - {self.data}"
