# Generated by Django 3.2 on 2021-05-07 23:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210507_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='assigned_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='assigned_to',
            field=models.ForeignKey(blank=True, limit_choices_to={'user_type': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]