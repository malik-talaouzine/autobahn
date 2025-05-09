# Generated by Django 5.2 on 2025-04-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_alter_station_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='coordinate',
        ),
        migrations.RemoveField(
            model_name='station',
            name='identifier',
        ),
        migrations.AddField(
            model_name='station',
            name='latitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='longitude',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
