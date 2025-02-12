# Generated by Django 4.2.3 on 2023-10-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0055_posts_support_favorite_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='support_follow_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='posts',
            name='support_views_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
