# Generated by Django 5.2 on 2025-04-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_alter_station_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
