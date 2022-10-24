# Generated by Django 3.2 on 2021-11-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20211114_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='complaints/photos/<function Photo.photo_dir at 0x2b01f6c3c280>'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='complaints/videos/<function Video.video_dir at 0x2b01f6c2edc0>'),
        ),
    ]