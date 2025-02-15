# Generated by Django 4.2.3 on 2023-11-05 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0033_adcampaigns_target_clicks_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMonthlyBillingSummary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.DateField()),
                ('total_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthly_billing_summaries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'month_year')},
            },
        ),
    ]
