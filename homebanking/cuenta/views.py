from rest_framework import viewsets, permissions
from .models import Cuenta
from .serializers import CuentaSerializer


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)