# Generated by Django 5.0.7 on 2024-07-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actors', models.IntegerField()),
                ('comment', models.IntegerField()),
                ('title_kor', models.CharField(max_length=100)),
                ('title_eng', models.CharField(max_length=100)),
                ('poster_url', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('showtime', models.CharField(max_length=100)),
                ('release_date', models.DateField(max_length=100)),
                ('plot', models.CharField(max_length=1000)),
                ('rating', models.CharField(max_length=100)),
                ('director_name', models.CharField(max_length=100)),
                ('director_image_url', models.CharField(max_length=500)),
            ],
        ),
    ]
