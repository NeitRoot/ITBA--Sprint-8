from django.db import models

# Create your models here.


class Marcas(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Marca"

    def __str__(self) -> str:
        return self.name


class Tarjetas(models.Model):
    id_card = models.AutoField(primary_key=True)
    card_number = models.TextField()
    cvv = models.TextField(db_column='CVV')
    grant_date = models.TextField()
    expiration_date = models.TextField()
    card_type = models.TextField()
    brand = models.ForeignKey(Marcas, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        ordering = ['id_card']
        verbose_name = "Tarjeta"

    def __str__(self) -> str:
        return self.card_type
