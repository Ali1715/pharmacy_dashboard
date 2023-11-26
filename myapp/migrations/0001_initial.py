# Generated by Django 4.2.7 on 2023-11-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.BigIntegerField()),
                ('fecha', models.DateTimeField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nota', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=1)),
                ('clienteID', models.IntegerField()),
                ('usuarioID', models.IntegerField()),
            ],
        ),
    ]
