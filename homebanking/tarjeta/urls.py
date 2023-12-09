from django.urls import path
from .views import TarjetaDetail, TarjetaCliente

urlpatterns = [
    path('tarjeta/<int:pk>', TarjetaDetail.as_view(), name='tarjeta-detail'),
    path('cliente/<int:pk>/tarjeta/', TarjetaCliente.as_view(), name='clientes-tarjetas')
]