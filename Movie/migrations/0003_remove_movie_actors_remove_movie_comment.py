# Generated by Django 5.0.7 on 2024-07-15 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0002_actor_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
    ]
