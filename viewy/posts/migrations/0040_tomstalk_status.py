# Generated by Django 4.2.3 on 2023-09-13 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0039_rename_caption_tomstalk_content_alter_tomstalk_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tomstalk',
            name='status',
            field=models.CharField(default='アンバサダー', max_length=25),
        ),
    ]
