# Generated by Django 4.2.3 on 2023-11-05 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0034_usermonthlybillingsummary'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermonthlybillingsummary',
            name='total_fee_with_tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
