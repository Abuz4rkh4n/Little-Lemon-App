# Generated by Django 4.1.7 on 2023-02-28 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='BookingDate',
            new_name='booking_date',
        ),
    ]
