# Generated by Django 4.2.7 on 2023-12-02 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0002_alter_tipodecuenta_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipodecuenta',
            options={'ordering': ['id'], 'verbose_name': 'Tipo_De_Cuenta'},
        ),
    ]