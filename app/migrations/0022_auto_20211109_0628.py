# Generated by Django 3.2 on 2021-11-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20211109_0627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='receiver',
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='complaints/photos/<function Photo.photo_dir at 0x2b6557751d30>'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='complaints/videos/<function Video.video_dir at 0x2b6557751e50>'),
        ),
    ]