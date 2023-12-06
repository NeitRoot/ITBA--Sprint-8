from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuentaViewSet, CuentasCliente

router = DefaultRouter()
router.register(r'cuenta', CuentaViewSet, basename='cuenta')

urlpatterns = [
    path('', include(router.urls)),
    path('clientes/<int:pk>/cuenta/', CuentasCliente.as_view(), name='clientes-cuentas'),
    path('cuenta/list/', CuentaViewSet.as_view({'get': 'list'}), name='cuenta-list'),
]


#http://127.0.0.1:8000/cuenta/clientes/1/cuenta/