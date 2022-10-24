# Generated by Django 3.2 on 2021-05-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tenant'), (2, 'Contractor'), (3, 'Data Officer'), (4, 'Admin')], default=1),
        ),
    ]