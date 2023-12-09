from django.db import models


from django.contrib.auth.models import User


class Cliente(models.Model):
    customer_name = models.TextField()
    customer_surname = models.TextField()
    customer_dni = models.TextField(db_column='customer_DNI')
    dob = models.TextField(blank=True, null=True)
    
    customer_adress = models.ForeignKey('direccion.Direccion', on_delete=models.CASCADE, default=None, null=True )
    type = models.CharField (max_length=10, default="CLASSIC", choices=(('BLACK', 'BLACK'), ('GOLD','GOLD'), ('CLASSIC', 'CLASSIC')))
    
    branch = models.ForeignKey('sucursal.Sucursal', models.DO_NOTHING)
    card = models.ForeignKey('tarjeta.Tarjetas', models.DO_NOTHING)

    username = models.OneToOneField(User, on_delete=models.CASCADE,  default=None, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Cliente"

    def __str__(self) -> str:
        return self.customer_name + " " + self.customer_surname + " "+ str(self.customer_dni)
