# Generated by Django 5.2 on 2025-04-11 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_alter_station_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
