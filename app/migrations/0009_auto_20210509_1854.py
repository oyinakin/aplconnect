# Generated by Django 3.2 on 2021-05-09 17:54

from django.db import migrations, models
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_complaint_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='Status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='resolutionlog',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Pending'), (2, 'Escalated'), (3, 'Resolved'), (4, 'Closed')], default=1),
        ),
        migrations.AddField(
            model_name='resolutionlog',
            name='time_of_action',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
