# Generated by Django 4.2.1 on 2023-06-04 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_remove_posts_location_delete_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='post_image',
        ),
        migrations.AddField(
            model_name='posts',
            name='file',
            field=models.FileField(default='', upload_to='media/files'),
        ),
    ]
