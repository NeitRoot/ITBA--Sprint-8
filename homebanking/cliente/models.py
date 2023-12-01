from django.db import models

# Create your models here.
from sucursal.models import Sucursal
from tarjeta.models import Tarjetas


class Cliente(models.Model):
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    branch = models.ForeignKey('sucursal.Sucursal', models.DO_NOTHING)
    card = models.ForeignKey('tarjeta.Tarjetas', models.DO_NOTHING)

    class Meta:
        ordering = ['customer_dni']
        verbose_name = "Cliente"

    def __str__(self) -> str:
        return self.customer_name
