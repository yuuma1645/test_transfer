# Generated by Django 4.2.3 on 2023-09-30 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0016_adinfos_clicks_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, verbose_name='社名')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
                ('address', models.CharField(max_length=255, verbose_name='住所')),
                ('phone_number', models.CharField(max_length=20, verbose_name='電話番号')),
            ],
        ),
    ]
