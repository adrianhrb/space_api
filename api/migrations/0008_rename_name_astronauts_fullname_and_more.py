# Generated by Django 5.0.1 on 2024-01-30 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_astronauts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='astronauts',
            old_name='name',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='astronauts',
            name='surname',
        ),
    ]
