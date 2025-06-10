from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Postagem, Comentario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Comentario
        fields = ['id', 'texto', 'usuario']

class PostagemSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    comentarios = ComentarioSerializer(many=True, read_only=True)

    class Meta:
        model = Postagem
        fields = ['id', 'titulo', 'conteudo', 'usuario', 'comentarios']
