# Generated by Django 3.2 on 2021-11-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_auto_20211113_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='complaints/photos/<function Photo.photo_dir at 0x2ab3739bf280>'),
        ),
        migrations.AlterField(
            model_name='video',
            name='videofile',
            field=models.FileField(upload_to='complaints/videos/<function Video.video_dir at 0x2ab3739b1dc0>'),
        ),
    ]
