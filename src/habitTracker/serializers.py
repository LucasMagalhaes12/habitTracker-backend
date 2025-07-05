from rest_framework import serializers
from .models import Habito, RegistroHabito
from django.contrib.auth.models import User

class RegistroHabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHabito
        fields = '__all__'

class HabitoSerializer(serializers.ModelSerializer):
    registros = RegistroHabitoSerializer(many=True, read_only=True)

    class Meta:
        model = Habito
        fields = [
            'id', 'nome', 'descricao', 'frequencia',
            'hora_sugerida', 'dias_semana', 'usuario', 'registros'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
