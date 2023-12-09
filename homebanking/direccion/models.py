from django.db import models

# Create your models here.
class Direccion(models.Model):
    address = models.TextField()

    class Meta:
        verbose_name = "Direccion"

    def __str__(self):
        return self.address
    