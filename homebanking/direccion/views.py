from .models import Direccion
from .serializers import DireccionSerializer
from cliente.models import Cliente
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response

class DireccionDetail(generics.RetrieveAPIView):
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer


class ClienteDireccion(APIView):
  
    def get(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        if cliente:
            direccion = cliente.customer_adress
            if direccion:
                serializer = DireccionSerializer(direccion)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Dirección no encontrada para este cliente", status=status.HTTP_404_NOT_FOUND)
        return Response("Cliente no encontrado", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        cliente = Cliente.objects.filter(pk=pk).first()
        if not cliente:
            return Response("Cliente no encontrado", status=status.HTTP_404_NOT_FOUND)
    
        direccion = Direccion.objects.filter(pk=cliente.customer_adress.id).first()
        if not direccion:
            return Response("Dirección no encontrada", status=status.HTTP_404_NOT_FOUND)

        serializer = DireccionSerializer(direccion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


