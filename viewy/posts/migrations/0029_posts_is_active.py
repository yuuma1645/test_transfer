# Generated by Django 4.2.3 on 2023-09-11 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_posts_qp_alter_viewdurations_post_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
