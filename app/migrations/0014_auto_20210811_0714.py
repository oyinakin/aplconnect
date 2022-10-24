# Generated by Django 3.2 on 2021-08-11 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20210807_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='complaints/photos/<function Photo.photo_dir at 0x2b6661bb7160>'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='complaints/videos/<function Video.video_dir at 0x2b6661ba8af0>'),
        ),
    ]
