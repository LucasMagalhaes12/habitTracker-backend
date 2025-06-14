from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Rotina

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class RotinaSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Rotina
        fields = ['id', 'nome', 'descricao', 'criado_em', 'usuario']
