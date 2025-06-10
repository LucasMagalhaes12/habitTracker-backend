from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RotinaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'rotinas', RotinaViewSet, basename='rotinas')
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]