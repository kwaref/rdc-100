# Generated by Django 4.0.1 on 2022-01-17 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_rename_name_post_title_remove_post_clip_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='clip',
            field=models.FileField(default='gh', upload_to=''),
            preserve_default=False,
        ),
    ]
