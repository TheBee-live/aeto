# Generated by Django 3.0.4 on 2021-08-21 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0004_auto_20210820_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='clase',
            field=models.CharField(choices=[('AUTOTANQUE ALIMENTICIO', 'Autotanque Alimenticio'), ('AUTOTANQUE COMBUSTIBLE', 'Autotanque Combustible'), ('AUTOTANQUE QUIMICOS', 'Autotanque Químicos'), ('CAJA REFRIGERADO 48', 'Caja Refrigerado 48'), ('CAJA SECA 40', 'Caja Seca 40'), ('CAJA SECA 48', 'Caja Seca 48'), ('CAJA SECA 53', 'Caja Seca 53'), ('CAJA SECA 53 (3 EJES)', 'Caja Seca 53 (3 Ejes)'), ('CAMIONETA', 'Camioneta'), ('CORTINA', 'Cortina'), ('CORTINA 38', 'Cortina 38'), ('DOLLY', 'Dolly'), ('PLATAFORMA 35', 'Plataforma 35'), ('PLATAFORMA 40', 'Plataforma 40'), ('PLATAFORMA 53', 'Plataforma 53'), ('PLATAFORMA 53 (3 EJES)', 'Plataforma 53 (3 Ejes)'), ('PORTACONTENEDOR', 'Portacontenedor'), ('RABON', 'Rabon'), ('THERMOKING THORTON CAJA 25', 'Thermoking Thorton Caja 25'), ('TOLVA', 'Tolva'), ('TORTHON REFRIGERADO', 'Torthon Refrigerado'), ('TORTHON SECO', 'Torthon Seco'), ('TRACTOCAMION', 'Tractocamion'), ('UTILITARIO TALLER', 'Utilitario Taller'), ('UTILITARIO ADMINISTRATIVO', 'Utilitario Administrativo'), ('YARD TRUCK', 'Yard Truck')], default='Tractor', max_length=200, null=True),
        ),
    ]
