# Generated by Django 4.2.3 on 2023-10-27 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0021_adcampaigns_target_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyadcost',
            name='cpc',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='monthlyadcost',
            name='cpm',
            field=models.IntegerField(),
        ),
    ]
