# Generated by Django 4.2.7 on 2023-12-04 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0006_alter_cuenta_account_type_delete_tipodecuenta'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDeCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'TipoDeCuenta',
                'ordering': ['type'],
            },
        ),
        migrations.AlterField(
            model_name='cuenta',
            name='account_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuenta.tipodecuenta'),
        ),
    ]
