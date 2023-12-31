# Generated by Django 4.2.7 on 2023-12-06 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
        ('cliente', '0004_rename_user_cliente_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='customer_adress',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='direccion.direccion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='type',
            field=models.CharField(choices=[('BLACK', 'BLACK'), ('GOLD', 'GOLD'), ('CLASSIC', 'CLASSIC')], default='CLASSIC', max_length=10),
        ),
    ]
