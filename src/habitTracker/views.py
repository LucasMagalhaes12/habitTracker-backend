from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Habito, RegistroHabito
from .serializers import HabitoSerializer, RegistroHabitoSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.decorators import api_view, permission_classes
from datetime import date, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import RegistroHabito

class HabitoViewSet(viewsets.ModelViewSet):
    queryset = Habito.objects.all()
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class RegistroHabitoViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroHabitoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RegistroHabito.objects.filter(habito__usuario=self.request.user)

    def perform_create(self, serializer):
        if serializer.validated_data['habito'].usuario != self.request.user:
            raise PermissionDenied("Você não tem permissão para registrar este hábito.")
        serializer.save()



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def marcar_habito_como_feito(request, habito_id):
   
    data_hoje = date.today()

    try:
        habito = Habito.objects.get(id=habito_id, usuario=request.user)
    except Habito.DoesNotExist:
        return Response({'error': 'Hábito não encontrado'}, status=status.HTTP_404_NOT_FOUND)

    
    RegistroHabito.objects.create(
        habito=habito,
        data=data_hoje,
        feito=True
    )

    return Response({'status': 'Hábito marcado como feito!'}, status=status.HTTP_201_CREATED)

def progresso_semanal(request):
    hoje = date.today()
    inicio_semana = hoje - timedelta(days=hoje.weekday() + 1)  # domingo
    fim_semana = inicio_semana + timedelta(days=6)             # sábado

    registros = RegistroHabito.objects.filter(
        habito__usuario=request.user,
        data__range=(inicio_semana, fim_semana),
        feito=True
    )

    total_realizados = registros.count()
    
    return Response({'realizados': total_realizados})
