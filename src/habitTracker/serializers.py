from rest_framework import serializers
from .models import Habito, RegistroHabito
from django.contrib.auth.models import User

class RegistroHabitoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHabito
        fields = '__all__'

class HabitoSerializer(serializers.ModelSerializer):
    registros = RegistroHabitoSerializer(many=True, read_only=True)
    done_dates = serializers.SerializerMethodField()  # ✅ ADICIONE ISSO

    class Meta:
        model = Habito
        fields = [
            'id', 'nome', 'descricao', 'frequencia',
            'hora_sugerida', 'dias_semana', 'usuario',
            'registros', 'done_dates'  # ✅ INCLUA AQUI
        ]

    def get_done_dates(self, obj):
        registros = obj.registros.all()  # ✅ ou obj.registrohabito_set.all() se não tiver related_name
        return [r.data.isoformat() for r in registros]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
