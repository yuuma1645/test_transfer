# Generated by Django 4.2.3 on 2023-08-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0016_ads_prf_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='prf_img',
            field=models.ImageField(default='ads_prf_imgs\\広告アイコン.png', upload_to='ads_prf_imgs'),
        ),
    ]
