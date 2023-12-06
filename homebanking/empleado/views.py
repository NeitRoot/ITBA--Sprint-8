
# Create your views here.
from rest_framework import viewsets, permissions
from .models import Empleado
from .serializers import EmpleadoSerializer


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)