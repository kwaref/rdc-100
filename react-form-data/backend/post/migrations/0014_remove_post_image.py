# Generated by Django 4.0.1 on 2022-01-17 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_post_clip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
