from django.db import models

# Create your models here.


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        ordering = ['branch_id']
        verbose_name = "Sucursal"

    def __str__(self) -> str:
        return self.branch_name
