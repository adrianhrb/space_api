# Generated by Django 5.0.1 on 2024-01-28 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_spacemissions_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spacemissions',
            name='rocketStatus',
            field=models.CharField(max_length=255),
        ),
    ]