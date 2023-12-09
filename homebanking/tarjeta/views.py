from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Tarjetas
from .serializers import TarjetaSerializer

# Create your views here.

class TarjetaDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Tarjetas.objects.all()
    serializer_class = TarjetaSerializer

class TarjetaCliente(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        cuentas = Tarjetas.objects.filter(cliente = pk)
        serializer = TarjetaSerializer(cuentas, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)