# Generated by Django 4.0.1 on 2022-01-17 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_rename_clip_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='clip',
            field=models.FileField(default='uy', upload_to=''),
            preserve_default=False,
        ),
    ]
