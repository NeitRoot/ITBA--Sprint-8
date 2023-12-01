# Generated by Django 4.2.7 on 2023-12-01 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sucursal', '0001_initial'),
        ('tarjeta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.TextField()),
                ('customer_surname', models.TextField()),
                ('customer_dni', models.TextField(db_column='customer_DNI')),
                ('dob', models.TextField(blank=True, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sucursal.sucursal')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tarjeta.tarjetas')),
            ],
            options={
                'verbose_name': 'Cliente',
                'ordering': ['customer_dni'],
            },
        ),
    ]
