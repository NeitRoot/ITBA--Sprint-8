from rest_framework import serializers
from .models import Sucursal


class SucursalSerializer(serializers.ModelSerializer):
    cliente =  serializers.ReadOnlyField(source = 'cliente.name')
    class Meta:
        model = Sucursal
        fields = '__all__'
        depth = 1
        read_only_fields = ['id', 'branch_number', 'branch_name', 'branch_adress_id']