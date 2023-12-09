from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cuenta
from .serializers import CuentaSerializer


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.all()
    serializer_class = CuentaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CuentasCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        cuentas = Cuenta.objects.filter(customer_id = pk)
        serializer = CuentaSerializer(cuentas, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)