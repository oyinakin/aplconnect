# Generated by Django 3.2 on 2021-05-08 00:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20210508_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='Status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Escalated'), (3, 'Resolved'), (4, 'Closed')], default=1),
        ),
        migrations.CreateModel(
            name='ResolutionLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_of_action', models.DateTimeField()),
                ('date_logged', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
