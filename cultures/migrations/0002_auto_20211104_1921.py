# Generated by Django 3.2.9 on 2021-11-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cultures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culture',
            name='discard_reason',
            field=models.CharField(
                blank=True,
                choices=[('male', 'Male'), ('pest', 'Pest')],
                max_length=4,
                null=True,
                verbose_name='Discard Reason',
            ),
        ),
        migrations.AlterField(
            model_name='culture',
            name='drying_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='culture',
            name='drying_weight',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name='culture',
            name='flowering_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='culture',
            name='harvest_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='culture',
            name='harvest_weight',
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name='culture',
            name='storage_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
