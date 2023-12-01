from django.db import models
from cliente.models import Cliente
# Create your models here.


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer = models.ForeignKey('cliente.Cliente', models.DO_NOTHING)

    class Meta:
        ordering = ['loan_id']
        verbose_name = "Prestamo"

    def __str__(self) -> str:
        return self.loan_type
