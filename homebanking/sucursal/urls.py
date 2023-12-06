from django.urls import path
from .views import SucursalPrestamos

urlpatterns = [
    path('prestamo/sucursal/<int:pk>/prestamo/', SucursalPrestamos.as_view(), name='sucursal-prestamo'),
]
