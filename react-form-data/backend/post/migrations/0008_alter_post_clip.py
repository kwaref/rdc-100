# Generated by Django 4.0.1 on 2022-01-17 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_alter_post_clip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='clip',
            field=models.ImageField(upload_to='post_images'),
        ),
    ]
