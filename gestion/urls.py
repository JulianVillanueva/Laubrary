from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LibroViewSet, PrestamoViewSet, RecordatorioDevolucionViewSet

router = DefaultRouter()
router.register(r'libro', LibroViewSet)
router.register(r'prestamo', PrestamoViewSet)
router.register(r'recordatoriodevolucion', RecordatorioDevolucionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
