# Generated by Django 4.2.7 on 2023-12-01 01:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['id'], 'verbose_name': 'Cliente'},
        ),
    ]
