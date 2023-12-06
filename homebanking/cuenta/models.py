from django.db import models

# Create your models here.

# class TipoDeCuenta(models.Model):
#     type = models.TextField(blank=True, null=True)

#     class Meta:
#         ordering = ['type']
#         verbose_name = "TipoDeCuenta"

#     def __str__(self) -> str:
#         return self.type

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('cliente.Cliente', models.DO_NOTHING)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.CharField(max_length=50, default='CUENTA CORRIENTE EN PESOS', choices=(('CUENTA CORRIENTE EN PESOS', 'CUENTA CORRIENTE EN PESOS'), ('CUENTA CORRIENTE EN DÓLARES','CUENTA CORRIENTE EN DÓLARES'), ('CAJA DE AHORRO EN PESOS', 'CAJA DE AHORRO EN PESOS'), ('CAJA DE AHORRO EN DÓLARES', 'CAJA DE AHORRO EN DÓLARES'), ('CUENTA INVERSIÓN', 'CUENTA INVERSIÓN')))

    class Meta:
        ordering = ['account_id']
        verbose_name = "Cuenta"

    def __str__(self) -> str:
        return self.account_type