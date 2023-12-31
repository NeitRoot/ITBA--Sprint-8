from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from cliente.models import Cliente
from prestamo.models import Prestamo
from prestamo.serializers import PrestamoSerializer

#obtener los clientes asociados a una sucursal específica y luego los préstamos relacionados con esos clientes
class SucursalPrestamos(APIView):
    permission_classes = [permissions.IsAuthenticated]  
    
    def get(self, request, sucursal_id):
        
        clientes_sucursal = Cliente.objects.filter(branch_id=sucursal_id)
        
        prestamos_sucursal = Prestamo.objects.filter(cliente__in=clientes_sucursal)
        
        serializer = PrestamoSerializer(prestamos_sucursal, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #REVER
