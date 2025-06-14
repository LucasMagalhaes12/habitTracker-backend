from rest_framework import viewsets, permissions
from .models import Habito, RegistroHabito
from .serializers import HabitoSerializer, RegistroHabitoSerializer
from rest_framework.permissions import IsAuthenticated

class HabitoViewSet(viewsets.ModelViewSet):
    queryset = Habito.objects.all()
    serializer_class = HabitoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

class RegistroHabitoViewSet(viewsets.ModelViewSet):
    queryset = Habito.objects.all()
    serializer_class = RegistroHabitoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return RegistroHabito.objects.filter(habito__usuario=self.request.user)
