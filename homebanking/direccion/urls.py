from django.urls import path

from .views import ClienteDireccion, DireccionDetail



urlpatterns = [
    path('cliente/<int:pk>/direccion/', ClienteDireccion.as_view(), name='cliente-direccion'),
    path('direccion/<int:pk>/', DireccionDetail.as_view(), name='direccion-detail'),
]