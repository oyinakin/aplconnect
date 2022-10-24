# Generated by Django 3.2 on 2021-11-15 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20211115_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='complaints/photos/<function Photo.photo_dir at 0x2abbfbc21280>'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='complaints/videos/<function Video.video_dir at 0x2abbfbc14dc0>'),
        ),
    ]