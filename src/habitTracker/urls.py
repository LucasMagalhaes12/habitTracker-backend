from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HabitoViewSet, RegistroHabitoViewSet

router = DefaultRouter()
router.register(r'habitos', HabitoViewSet, basename='habitos')
router.register(r'registros', RegistroHabitoViewSet, basename='registros')

urlpatterns = [
    path('', include(router.urls)),
]


