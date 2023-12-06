from rest_framework import viewsets, permissions
from .models import Cliente
from .serializers import ClienteSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        customer_data = serializer.validated_data

        try:
            user = User.objects.create_user(
                username=customer_data['customer_dni'], 
                password='contraseña_segura'
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            serializer.save(user=user)
        except Exception as e:
            user.delete()
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

#         datos_cliente = {
#             'id': cliente.id,
#             'nombre': cliente.customer_name,
#             'apellido': cliente.customer_lastname,
#             'dni':cliente.customer_dni,
#             'fecha de nacimiento': cliente.dob,
#             'sucursal': cliente.branch,
#             'tarjeta': cliente.card
#         }
