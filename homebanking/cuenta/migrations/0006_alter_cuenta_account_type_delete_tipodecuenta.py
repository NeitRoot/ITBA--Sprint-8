# Generated by Django 4.2.7 on 2023-12-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0005_alter_tipodecuenta_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='account_type',
            field=models.CharField(choices=[('CUENTA CORRIENTE EN PESOS', 'CUENTA CORRIENTE EN PESOS'), ('CUENTA CORRIENTE EN DÓLARES', 'CUENTA CORRIENTE EN DÓLARES'), ('CAJA DE AHORRO EN PESOS', 'CAJA DE AHORRO EN PESOS'), ('CAJA DE AHORRO EN DÓLARES', 'CAJA DE AHORRO EN DÓLARES'), ('CUENTA INVERSIÓN', 'CUENTA INVERSIÓN')], default='CUENTA CORRIENTE EN PESOS', max_length=50),
        ),
        migrations.DeleteModel(
            name='TipoDeCuenta',
        ),
    ]
