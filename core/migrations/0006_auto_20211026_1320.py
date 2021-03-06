# Generated by Django 3.2.8 on 2021-10-26 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_aapl_open_data_appl_open'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='appl_adjusted',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='appl_close',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='appl_high',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='appl_low',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='appl_open',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='appl_volume',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='dn',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='mavg',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='up',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=100, null=True),
        ),
    ]
