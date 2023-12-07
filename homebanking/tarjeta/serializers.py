from rest_framework import serializers
from .models import Tarjetas


class TarjetaSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField(source='cliente.customer_name')
    class Meta:
        model = Tarjetas
        fields = "__all__"
        depth = 1
        read_only_fields = ['id']