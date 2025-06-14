from rest_framework import viewsets, permissions
from .models import Rotina
from .serializers import RotinaSerializer
from django.contrib.auth.models import User
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class RotinaViewSet(viewsets.ModelViewSet):
    serializer_class = RotinaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Rotina.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
