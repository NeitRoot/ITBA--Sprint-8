from django.db import models

# Create your models here.


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')
    branch_id = models.IntegerField()

    class Meta:
        ordering = ['employee_id']
        verbose_name = "Empleado"

    def __str__(self) -> str:
        return self.employee_name
