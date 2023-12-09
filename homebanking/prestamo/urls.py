from django.urls import path, include
from .views import PrestamoDetail, PrestamosCliente, PrestamoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'prestamo', PrestamoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('prestamos/<int:pk>/', PrestamoDetail.as_view(), name='prestamo-detail'),
    path('clientes/<int:pk>/prestamos/', PrestamosCliente.as_view(), name='clientes-prestamos')
]

#http://127.0.0.1:8000/prestamo/clientes/1/prestamos/