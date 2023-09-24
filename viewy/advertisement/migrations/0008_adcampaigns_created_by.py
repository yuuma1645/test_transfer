# Generated by Django 4.2.3 on 2023-09-19 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisement', '0007_adinfos_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='adcampaigns',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_campaigns', to=settings.AUTH_USER_MODEL),
        ),
    ]
