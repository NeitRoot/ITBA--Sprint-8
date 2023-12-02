from django.db import models

# Create your models here.

class TipoDeCuenta(models.Model):
    type = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['type']
        verbose_name = "TipoDeCuenta"

    def __str__(self) -> str:
        return self.type

class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('cliente.Cliente', models.DO_NOTHING)
    balance = models.IntegerField()
    iban = models.TextField()
    account_type = models.ForeignKey(TipoDeCuenta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['account_id']
        verbose_name = "Cuenta"

    def __str__(self) -> str:
        return self.account_type