from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Prestamo
from cliente.models import Cliente
from .serializers import PrestamoSerializer
from cuenta.models import Cuenta
from django.shortcuts import get_object_or_404
from django.db import transaction

# Create your views here.

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
         serializer.save(owner=self.request.user)

class PrestamoDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, pk):
        prestamos = Prestamo.objects.filter(pk = pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def delete(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        cuenta = Cuenta.objects.filter(cliente=prestamo.customer, tipo=1).first()

        if cuenta and prestamo:
            with transaction.atomic():
                cuenta.balance -= prestamo.loan_total
                cuenta.save()
                prestamo.delete()
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class PrestamosCliente(APIView):
    
    def get(self, request, pk):
        prestamos = Prestamo.objects.filter(customer = pk)
        serializer = PrestamoSerializer(prestamos, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    
    def post(self, request, pk, format = None):
        cuenta = Cuenta.objects.filter(customer = pk, tipo__exact = 1).first()
        cuenta = Cuenta.objects.filter(customer = pk, ).first()
        serializer = PrestamoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(cliente = Cliente.objects.filter(pk=pk).first())
            cuenta.balance = cuenta.balance + int(serializer.data['loan_total'])
            cuenta.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)