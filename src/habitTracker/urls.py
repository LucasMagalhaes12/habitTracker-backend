from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitoViewSet, RegistroHabitoViewSet
from habitTracker.views import HabitoViewSet, RegistroHabitoViewSet
from .views import marcar_habito_como_feito
from .views import progresso_semanal

router = DefaultRouter()
router.register(r'habitos', HabitoViewSet, basename='habitos')
router.register(r'registros', RegistroHabitoViewSet, basename='registros')



urlpatterns = [
    path('', include(router.urls)),
    path('habitos/<int:habito_id>/feito/', marcar_habito_como_feito),  # ✅ nova rota
    path('habitos/progresso-semanal/', progresso_semanal),

]


